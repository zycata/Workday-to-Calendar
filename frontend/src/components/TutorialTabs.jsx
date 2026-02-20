import { useState } from 'react';
import './TutorialTabs.css';
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
          <embed className="pdf-embed" src="/workday-download-guide.pdf" type="application/pdf" />
        )}
        {activeTab === 'tab2' && (
          <embed className="pdf-embed" src="/sample_pdf.pdf" type="application/pdf" />
        )}
      </div>
    </div>
  );
}

export default TutorialTabs;