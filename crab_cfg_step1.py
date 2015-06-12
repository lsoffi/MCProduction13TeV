from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'Higgs_scalar_nohdecay_gg_1GeV_13TeV'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'PrivateMC'
config.JobType.generator = 'lhe'
config.JobType.psetName = 'step1.py'
config.JobType.inputFiles = ['/afs/cern.ch/user/s/soffi/public/Higgs_scalar_nohdecay_1GeV_13TeV.lhe']

config.Data.primaryDataset = 'MinBias'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 100
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#config.Data.outLFN = '/store/user/dburns/' # or '/store/group/<subdir>'
config.Data.publication = True
config.Data.publishDataName = 'Higgs_scalar_nohdecay_gg_1GeV_13TeV'

#config.Site.blacklist = ["T2_US_UCSD"]
config.Site.storageSite = 'T2_IT_Rome'

