import { useState } from 'react';
import './TutorialTabs.css';

import workday_guide from '../assets/workday-download-guide.pdf'
import sample_pdf from '../assets/sample_pdf.pdf'
function TutorialTabs() {
  const [activeTab, setActiveTab] = useState('tab1');

  return (
    <div className="tabs-wrapper">
      {/* 1. The Tab Buttons */}
      <div className="tab-buttons">
        <button
          className={activeTab === 'tab1' ? 'active' : ''}
          onClick={() => setActiveTab('tab1')}
        >
          Download schedule from workday
        </button>
        <button
          className={activeTab === 'tab2' ? 'active' : ''}
          onClick={() => setActiveTab('tab2')}
        >
          Uploading to a calendar service
        </button>
      </div>

      {/* 2. The Content Area */}
      <div className="tab-content">
        {activeTab === 'tab1' && (
          <embed className="pdf-embed" src={workday_guide} type="application/pdf" />
        )}
        {activeTab === 'tab2' && (
          <embed className="pdf-embed" src={sample_pdf} type="application/pdf" />
        )}
      </div>
    </div>
  );
}

export default TutorialTabs;