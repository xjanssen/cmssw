import FWCore.ParameterSet.Config as cms

SingleTopSingleMuonHLTOfflineDQM = cms.EDAnalyzer("TopSingleLeptonHLTOfflineDQM",
  ## ------------------------------------------------------
  ## SETUP
  ##
  ## configuration of the MonitoringEnsemble(s)
  ## [mandatory] : optional PSets may be omitted
  ##
  setup = cms.PSet(
    ## sub-directory to write the monitor histograms to
    ## [mandatory] : should not be changed w/o explicit
    ## communication to TopCom!
    directory = cms.string("HLT/TopHLTOffline/SingleTop/SingleMuon/"),
    ## [mandatory]
    sources = cms.PSet(
      muons = cms.InputTag("muons"),
      elecs = cms.InputTag("gedGsfElectrons"),
      jets  = cms.InputTag("ak4PFJetsCHS"),
      mets  = cms.VInputTag("met", "tcMet", "pfMet"),
      pvs   = cms.InputTag("offlinePrimaryVertices")

    ),
    ## [optional] : when omitted all monitoring plots for primary vertices
    ## will be filled w/o extras
    pvExtras = cms.PSet(
      ## when omitted electron plots will be filled w/o additional pre-
      ## selection of the primary vertex candidates                                                                                            
      select = cms.string("abs(x)<1. & abs(y)<1. & abs(z)<20. & tracksSize>3 & !isFake")
    ),
    ## [optional] : when omitted all monitoring plots for muons
    ## will be filled w/o extras                                           
    muonExtras = cms.PSet(
      ## when omitted muon plots will be filled w/o additional pre-
      ## selection of the muon candidates                                                
      select = cms.string("pt>26 & abs(eta)<2.1 & isPFMuon & isGlobalMuon & globalTrack.normalizedChi2<10 & innerTrack.hitPattern.trackerLayersWithMeasurement>5 & innerTrack.hitPattern.numberOfValidPixelHits>0 & numberOfMatches>1"),
      ## when omitted isolated muon multiplicity plot will be equi-
      ## valent to inclusive muon multiplicity plot                                                    
      isolation = cms.string("(pfIsolationR04.sumChargedHadronPt+pfIsolationR04.sumPhotonEt+pfIsolationR04.sumNeutralHadronEt)/pt<0.2"),
    ),
    ## [optional] : when omitted all monitoring plots for jets
    ## will be filled w/o extras
    jetExtras = cms.PSet(
      ## when omitted monitor plots for pt will be filled from uncorrected
      ## jets
      #jetCorrector = cms.string("ak4PFCHSL2L3"),
      ## when omitted no extra selection will be applied on jets before
      ## filling the monitor histograms; if jetCorrector is present the
      ## selection will be applied to corrected jets                                                
      select = cms.string("pt>40 & abs(eta)<5.0"),
      ## when omitted monitor histograms for b-tagging will not be filled 
      jetBTaggers  = cms.PSet(
         trackCountingEff = cms.PSet(
           label = cms.InputTag("jetProbabilityBJetTags" ),
           workingPoint = cms.double(0.275)
         ),
         trackCountingPur = cms.PSet(
           label = cms.InputTag("trackCountingHighPurBJetTags" ),
           workingPoint = cms.double(3.41)
         ),
         secondaryVertex  = cms.PSet(
           label = cms.InputTag("combinedSecondaryVertexBJetTags"),
           workingPoint = cms.double(0.679)
         )
       ),
    ),
    ## [optional] : when omitted no mass window will be applied
    ## for the W mass before filling the event monitoring plots
    massExtras = cms.PSet(
      lowerEdge = cms.double( 70.),
      upperEdge = cms.double(110.)
    ),
    ## [optional] : when omitted the monitoring plots for triggering
    ## will be empty
    triggerExtras = cms.PSet(
      src   = cms.InputTag("TriggerResults","","HLT"),
      paths = cms.vstring(['HLT_IsoMu24_IterTrk02_v', 'HLT_IsoMu24_IterTrk02_TriCentralPFJet60_50_35_v', 'HLT_IsoMu24_IterTrk02_TriCentralPFJet40_v', 'HLT_IsoMu24_IterTrk02_CentralPFJet30_BTagCSV_v', 'HLT_IsoMu20_eta2p1_IterTrk02_CentralPFJet30_BTagCSV_v', 'HLT_IsoMu20_eta2p1_IterTrk02_TriCentralPFJet40_v', 'HLT_IsoMu20_eta2p1_IterTrk02_TriCentralPFJet60_50_35_v', 'HLT_IsoMu20_eta2p1_IterTrk02_v', 'HLT_IsoTkMu20_eta2p1_IterTrk02_v', 'HLT_IsoMu24_eta2p1_IterTrk02_CentralPFJet30_BTagCSV_v', 'HLT_IsoMu24_eta2p1_IterTrk02_TriCentralPFJet40_v', 'HLT_IsoMu24_eta2p1_IterTrk02_TriCentralPFJet60_50_35_v', 'HLT_IsoMu24_eta2p1_IterTrk02_v', 'HLT_IsoTkMu24_eta2p1_IterTrk02_v'])
    )
  ),
  ## ------------------------------------------------------
  ## PRESELECTION
  ##
  ## setup of the event preselection, which will not
  ## be monitored
  ## [mandatory] : but may be empty
  ##
  preselection = cms.PSet(
    trigger = cms.PSet(
      src    = cms.InputTag("TriggerResults","","HLT"),
      select = cms.vstring(['HLT_IsoMu24_IterTrk02_v', 'HLT_IsoMu24_IterTrk02_TriCentralPFJet60_50_35_v', 'HLT_IsoMu24_IterTrk02_TriCentralPFJet40_v', 'HLT_IsoMu24_IterTrk02_CentralPFJet30_BTagCSV_v', 'HLT_IsoMu20_eta2p1_IterTrk02_CentralPFJet30_BTagCSV_v', 'HLT_IsoMu20_eta2p1_IterTrk02_TriCentralPFJet40_v', 'HLT_IsoMu20_eta2p1_IterTrk02_TriCentralPFJet60_50_35_v', 'HLT_IsoMu20_eta2p1_IterTrk02_v', 'HLT_IsoTkMu20_eta2p1_IterTrk02_v', 'HLT_IsoMu24_eta2p1_IterTrk02_CentralPFJet30_BTagCSV_v', 'HLT_IsoMu24_eta2p1_IterTrk02_TriCentralPFJet40_v', 'HLT_IsoMu24_eta2p1_IterTrk02_TriCentralPFJet60_50_35_v', 'HLT_IsoMu24_eta2p1_IterTrk02_v', 'HLT_IsoTkMu24_eta2p1_IterTrk02_v'])
    ),
    ## [optional] : when omitted no preselection is applied
    vertex = cms.PSet(
      src    = cms.InputTag("offlinePrimaryVertices"),
      select = cms.string('abs(x)<1. & abs(y)<1. & abs(z)<20. & tracksSize>3 & !isFake')
    )                                       
  ), 
  ## ------------------------------------------------------
  ## SELECTION
  ##
  ## monitor histrograms are filled after each selection
  ## step, the selection is applied in the order defined
  ## by this vector
  ## [mandatory] : may be empty or contain an arbitrary
  ## number of PSets
  selection = cms.VPSet(
    cms.PSet(
      label  = cms.string("Hlt:step0"),
      src    = cms.InputTag(""),
      select = cms.string(""),
      min    = cms.int32(0),
      max    = cms.int32(0),
    ),
    cms.PSet(
      label  = cms.string("muons:step1"),
      src    = cms.InputTag("muons"),
      select = cms.string("pt>26 & abs(eta)<2.1 & isPFMuon & isGlobalMuon & globalTrack.normalizedChi2<10 & innerTrack.hitPattern.trackerLayersWithMeasurement>5 & innerTrack.hitPattern.numberOfValidPixelHits>0 & numberOfMatches>1 & (pfIsolationR04.sumChargedHadronPt+pfIsolationR04.sumPhotonEt+pfIsolationR04.sumNeutralHadronEt)/pt<0.12"),
      min    = cms.int32(1),
      max    = cms.int32(1),
    ),
    #cms.PSet(
    #  label  = cms.string("jets/pf:step2"),
    #  src    = cms.InputTag("ak4PFJetsCHS"),
    #  jetCorrector = cms.string("ak4PFCHSL2L3"),
    #  select = cms.string("pt>40 & abs(eta)<5.0"),
    #  min = cms.int32(1),
    #), 
    cms.PSet(
      label  = cms.string("jets/pf:step2"),
      src    = cms.InputTag("ak4PFJetsCHS"),
      #jetCorrector = cms.string("ak4PFCHSL2L3"),
      select = cms.string("pt>40 & abs(eta)<5.0"),
      min = cms.int32(2),
    ), 
  )
)

SingleTopSingleElectronHLTOfflineDQM = cms.EDAnalyzer("TopSingleLeptonHLTOfflineDQM",
  ## ------------------------------------------------------
  ## SETUP
  ##
  ## configuration of the MonitoringEnsemble(s)
  ## [mandatory] : optional PSets may be omitted
  ##
  setup = cms.PSet(
    ## sub-directory to write the monitor histograms to
    ## [mandatory] : should not be changed w/o explicit
    ## communication to TopCom!
    directory = cms.string("HLT/TopHLTOffline/SingleTop/SingleElectron/"),
    ## [mandatory]
    sources = cms.PSet(
      muons = cms.InputTag("muons"),
      elecs = cms.InputTag("gedGsfElectrons"),
      jets  = cms.InputTag("ak4PFJetsCHS"),
      mets  = cms.VInputTag("met", "tcMet", "pfMet"),
      pvs   = cms.InputTag("offlinePrimaryVertices")

    ),
    ## [optional] : when omitted all monitoring plots for primary vertices
    ## will be filled w/o extras
    pvExtras = cms.PSet(
      ## when omitted electron plots will be filled w/o additional pre-
      ## selection of the primary vertex candidates                                                                                            
      select = cms.string("abs(x)<1. & abs(y)<1. & abs(z)<20. & tracksSize>3 & !isFake")
    ),
    ## [optional] : when omitted all monitoring plots for electrons
    ## will be filled w/o extras
    elecExtras = cms.PSet(
      ## when omitted electron plots will be filled w/o cut on electronId
      #electronId = cms.PSet( src = cms.InputTag("mvaTrigV0"), pattern = cms.int32(1) ),
      ## when omitted electron plots will be filled w/o additional pre-
      ## selection of the electron candidates
      select = cms.string("pt>30 & abs(eta)<2.5"),
      ## when omitted isolated electron multiplicity plot will be equi-
      ## valent to inclusive electron multiplicity plot 
      isolation = cms.string("(dr03TkSumPt+dr04EcalRecHitSumEt+dr04HcalTowerSumEt)/pt<0.1"),
    ),
    ## [optional] : when omitted all monitoring plots for jets
    ## will be filled w/o extras
    jetExtras = cms.PSet(
      ## when omitted monitor plots for pt will be filled from uncorrected
      ## jets
      #jetCorrector = cms.string("ak4PFCHSL2L3"),
      ## when omitted no extra selection will be applied on jets before
      ## filling the monitor histograms; if jetCorrector is present the
      ## selection will be applied to corrected jets                                                
      select = cms.string("pt>40 & abs(eta)<5.0"),
      ## when omitted monitor histograms for b-tagging will not be filled  
      jetBTaggers  = cms.PSet(
         trackCountingEff = cms.PSet(
           label = cms.InputTag("jetProbabilityBJetTags" ),
           workingPoint = cms.double(0.275)
         ),
         trackCountingPur = cms.PSet(
           label = cms.InputTag("trackCountingHighPurBJetTags" ),
           workingPoint = cms.double(3.41)
         ),
         secondaryVertex  = cms.PSet(
           label = cms.InputTag("combinedSecondaryVertexBJetTags"),
           workingPoint = cms.double(0.679)
         )
       ),
    ),
    ## [optional] : when omitted no mass window will be applied
    ## for the W mass before filling the event monitoring plots
    massExtras = cms.PSet(
      lowerEdge = cms.double( 70.),
      upperEdge = cms.double(110.)
    ),
    ## [optional] : when omitted the monitoring plots for triggering
    ## will be empty
    triggerExtras = cms.PSet(
      src   = cms.InputTag("TriggerResults","","HLT"),
      paths = cms.vstring(['HLT_Ele27_eta2p1_WP85_Gsf_v', 'HLT_Ele27_eta2p1_WP85_Gsf_TriCentralPFJet40_v', 'HLT_Ele27_eta2p1_WP85_Gsf_TriCentralPFJet60_50_35_v', 'HLT_Ele27_eta2p1_WP85_Gsf_CentralPFJet30_BTagCSV_v', 'HLT_Ele32_WP85_Gsf_CentralPFJet30_BTagCSV_v', 'HLT_Ele32_WP85_Gsf_TriCentralPFJet40_v', 'HLT_Ele32_WP85_Gsf_TriCentralPFJet60_50_35_v', 'HLT_Ele32_WP85_Gsf_v'])
     )
  ),
  ## ------------------------------------------------------
  ## PRESELECTION
  ##
  ## setup of the event preselection, which will not
  ## be monitored
  ## [mandatory] : but may be empty
  ##
  preselection = cms.PSet(
    trigger = cms.PSet(
      src    = cms.InputTag("TriggerResults","","HLT"),
      select = cms.vstring(['HLT_Ele27_eta2p1_WP85_Gsf_v', 'HLT_Ele27_eta2p1_WP85_Gsf_TriCentralPFJet40_v', 'HLT_Ele27_eta2p1_WP85_Gsf_TriCentralPFJet60_50_35_v', 'HLT_Ele27_eta2p1_WP85_Gsf_CentralPFJet30_BTagCSV_v', 'HLT_Ele32_WP85_Gsf_CentralPFJet30_BTagCSV_v', 'HLT_Ele32_WP85_Gsf_TriCentralPFJet40_v', 'HLT_Ele32_WP85_Gsf_TriCentralPFJet60_50_35_v', 'HLT_Ele32_WP85_Gsf_v'])
     ),
    ## [optional] : when omitted no preselection is applied
    vertex = cms.PSet(
      src    = cms.InputTag("offlinePrimaryVertices"),
      select = cms.string('abs(x)<1. & abs(y)<1. & abs(z)<20. & tracksSize>3 & !isFake')
    )                                       
  ), 
  ## ------------------------------------------------------
  ## SELECTION
  ##
  ## monitor histrograms are filled after each selection
  ## step, the selection is applied in the order defined
  ## by this vector
  ## [mandatory] : may be empty or contain an arbitrary
  ## number of PSets
  selection = cms.VPSet(
    cms.PSet(
      label  = cms.string("Hlt:step0"),
      src    = cms.InputTag(""),
      select = cms.string(""),
      min    = cms.int32(0),
      max    = cms.int32(0),
    ),
    cms.PSet(
      label  = cms.string("elecs:step1"),
      src    = cms.InputTag("gedGsfElectrons"),
      #electronId = cms.PSet( src = cms.InputTag("mvaTrigV0"), pattern = cms.int32(1) ),
      select = cms.string("pt>30 & abs(eta)<2.5 & (dr03TkSumPt+dr04EcalRecHitSumEt+dr04HcalTowerSumEt)/pt<0.1"),
      min    = cms.int32(1),
      max    = cms.int32(1),
    ),
    #cms.PSet(
    #  label  = cms.string("jets/pf:step2"),
    #  src    = cms.InputTag("ak4PFJetsCHS"),
    #  jetCorrector = cms.string("ak4PFCHSL2L3"),
    #  select = cms.string("pt>40 & abs(eta)<5.0"),
    #  min = cms.int32(1),
    #), 
    cms.PSet(
      label  = cms.string("jets/pf:step2"),
      src    = cms.InputTag("ak4PFJetsCHS"),
      #jetCorrector = cms.string("ak4PFCHSL2L3"),
      select = cms.string("pt>40 & abs(eta)<5.0"),
      min = cms.int32(2),
    ), 
  )
)
