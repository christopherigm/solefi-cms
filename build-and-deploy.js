const { exec } = require('child_process');
const { exit } = require('process');
const https = require('https');
const axios = require('axios');
const name = 'solefi-api';
const args = process.argv;
const jenkinsURL = args && args.length &&
  args.length === 3 && args[2] === '--production' ? 
  `https://jenkins.solefi.com.mx/generic-webhook-trigger/invoke?token=${name}` :
  `https://jenkins.longmont.iguzman.com.mx/generic-webhook-trigger/invoke?token=${name}`;
const registry = 'registry.vaggustudios.com';
let branch = '';
const startTime = new Date(Date.now());

const instance = axios.create({
  httpsAgent: new https.Agent({
    rejectUnauthorized: false
  })
});

const triggerJenkinsJob = () => {
  return new Promise((res, rej) => {
    console.log('\n========= Triggering Jenkins Job =========');
    instance.post(jenkinsURL, {
      BRANCH: branch
    })
      .then((response) => {
        res(response.data);
      })
      .catch((error) => {
        rej(error);
      });
  });
};

const getBranchName = () => {
  return new Promise((res, rej) => {
    exec('git branch --show-current', (err, stdout) => {
      if (err) return rej(err);
      const branch = stdout.toString().replace(/(\r\n|\n|\r)/gm, '');
      res(branch);
    });
  });
};

const tagDockerImage = () => {
  return new Promise((res, rej) => {
    console.log('\n========= Tagging Docker Image =========');
    getBranchName()
      .then((data) => {
        branch = data;
        console.log('\nBranch:', branch);
        exec(`docker tag ${name} ${registry}/${name}:${branch}`, (err, stdout) => {
          if (err) return rej(err);
          console.log('\nDocker Image tagged!');
          res(stdout);
        });
      })
      .catch((err) => {
        console.log('\nBuild Docker image error:', err);
      });
  });
};

const publishDockerImage = () => {
  return new Promise((res, rej) => {
    console.log('\n========= Publishing Docker Image =========');
    getBranchName()
      .then((branch) => {
        exec(`docker push ${registry}/${name}:${branch}`, (err, stdout) => {
          if (err) return rej(err);
          console.log('\nDocker Image published!');
          res(stdout);
        });
      })
      .catch((err) => {
        console.log('\nBuild Docker image error:', err);
      });
  });
};

const buildDockerImage = () => {
  return new Promise((res, rej) => {
    console.log('\n========= Building Docker Image =========');
    exec(`docker build -t ${name} .`, (err, stdout) => {
      if (err) return rej(err);
      console.log('\nDocker Image built');
      res(stdout);
    });
  });
};

buildDockerImage()
  .then(() => tagDockerImage())
  .then(() => publishDockerImage())
  .then(() => triggerJenkinsJob())
  .then((response) => {
    if ( response && response.jobs &&
      response.jobs['Solefi-API'] &&
      response.jobs['Solefi-API'].triggered ) {
      console.log('\nProces completed!:', response.message);
      console.log(`\nImage: ${registry}/${name}:${branch}`);
    } else {
      console.log('\nError triggering Jenkins job:', response.response.statusText);
      console.log(`\nImage: ${registry}/${name}:${branch}`);
    }
    const endTime = new Date(Date.now());
    const difference = (((endTime - startTime)/100)/60)/60;
    console.log('\nStarting time:', startTime);
    console.log('Ending time:', endTime);
    console.log('Processing time:', Math.round((difference + Number.EPSILON) * 100) / 100, 'minutes.');
    exit(1);
  })
  .catch((err) => {
    console.log('\nError:', err);
    exit(1);
  });
