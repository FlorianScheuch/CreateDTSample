# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: MinBias_13TeV_cfi --step GEN,SIM --geometry Extended2015 --conditions auto:upgradePLS1 --pileup NoPileUp --datamix NODATAMIXER --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --eventcontent FEVTDEBUG --datatier GEN-SIM -n 10
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2015_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)


# Pooja's input
# from CondCore.DBCommon.CondDBSetup_cfi import *
# process.noisesfromprep = cms.ESSource("PoolDBESSource",
#                                       # connect = cms.string('sqlite_file:RPC_Phase2UpgradeStudies_mc.db'),                                                      
#                       # connect = cms.string('sqlite_file:RPC_Eff2012_PhaseII_mc.db'),    
#                                       # connect = cms.string('sqlite_file:RPC_Eff2012_256Strips_mc.db'),                                                    
#                                       # connect = cms.string('sqlite_file:RPC_dataDrivenCondition_RPCEta2Upscope_mc.db'),   
#                       connect = cms.string('sqlite_fip:L1Trigger/L1IntegratedMuonTrigger/data/RPC_3108Rolls_BkgAtLumi1_14TeV_mc.db'),
#                                       DBParameters = cms.PSet(
#         messageLevel = cms.untracked.int32(0),
#         authenticationPath = cms.untracked.string('.'),
#         authenticationMethod = cms.untracked.uint32(1)
#         ),
#                                       timetype = cms.string('runnumber'),
#                                       toGet = cms.VPSet(cms.PSet(
#             record = cms.string('RPCStripNoisesRcd'),
#             label = cms.untracked.string("noisesfromprep"),
#             # tag = cms.string('RPC_Phase2UpgradeStudies_mc')
#             # tag = cms.string('RPC_Eff2012_PhaseII_mc')
#             # tag = cms.string('RPC_Eff2012_256Strips_mc') 
#             # tag = cms.string('RPC_dataDrivenCondition_RPCEta2Upscope_mc')  
#             tag = cms.string('RPC_3108Rolls_BkgAtLumi1_14TeV_mc')
#             )
#                                                         )
#                                       )
# process.es_prefer_noisesfromprep=cms.ESPrefer("PoolDBESSource", "noisesfromprep")




# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('MinBias_13TeV_cfi nevts:11'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.FEVTDEBUGEventContent.outputCommands,
    fileName = cms.untracked.string('MinBias_13TeV_cfi_GEN_SIM.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
#from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgradePLS1', '')
from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, globalTag+'::All', '')

# http://cmslxr.fnal.gov/lxr/source/Configuration/AlCa/python/autoCond.py?view=markup
from Configuration.AlCa.autoCond import autoCond
process.GlobalTag.globaltag = autoCond['run2_mc'] #PRE_LS172_V15::All

process.generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(33)=0     ! no K factors in hard cross sections', 
            'MSTP(2)=1      ! which order running alphaS', 
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
            'MSTP(52)=2     ! work with LHAPDF', 
            'PARP(82)=1.921 ! pt cutoff for multiparton interactions', 
            'PARP(89)=1800. ! sqrts for which PARP82 is set', 
            'PARP(90)=0.227 ! Multiple interactions: rescaling power', 
            'MSTP(95)=6     ! CR (color reconnection parameters)', 
            'PARP(77)=1.016 ! CR', 
            'PARP(78)=0.538 ! CR', 
            'PARP(80)=0.1   ! Prob. colored parton from BBR', 
            'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter', 
            'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter', 
            'PARP(62)=1.025 ! ISR cutoff', 
            'MSTP(91)=1     ! Gaussian primordial kT', 
            'PARP(93)=10.0  ! primordial kT-max', 
            'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4     ! Defines the multi-parton model'),
        processParameters = cms.vstring('MSEL=0         ! User defined processes', 
            'MSUB(11)=1     ! Min bias process', 
            'MSUB(12)=1     ! Min bias process', 
            'MSUB(13)=1     ! Min bias process', 
            'MSUB(28)=1     ! Min bias process', 
            'MSUB(53)=1     ! Min bias process', 
            'MSUB(68)=1     ! Min bias process', 
            'MSUB(92)=1     ! Min bias process, single diffractive', 
            'MSUB(93)=1     ! Min bias process, single diffractive', 
            'MSUB(94)=1     ! Min bias process, double diffractive', 
            'MSUB(95)=1     ! Min bias process'),
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.FEVTDEBUGoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.
#process.RandomNumberGeneratorService.generator.initialSeed = 1
# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# End of customisation functions

