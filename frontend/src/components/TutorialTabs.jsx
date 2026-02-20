import { useState } from 'react';

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
          Workday Guide
        </button>
        <button
          className={activeTab === 'tab2' ? 'active' : ''}
          onClick={() => setActiveTab('tab2')}
        >
          Troubleshooting
        </button>
      </div>

      {/* 2. The Content Area */}
      <div className="tab-content">
        {activeTab === 'tab1' && (
          <embed className="pdf-embed" src="/invoicesample.pdf" type="application/pdf" />
        )}
        {activeTab === 'tab2' && (
          <embed className="pdf-embed" src="/sample_pdf.pdf" type="application/pdf" />
        )}
      </div>
    </div>
  );
}

export default TutorialTabs;