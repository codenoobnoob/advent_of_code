import type {Config} from '@jest/types';

// Sync object
const config: Config.InitialOptions = {
  verbose: true,
  testRegex: "./test/.*.ts$",
  rootDir: "."
};
export default config;
