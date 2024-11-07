import React, { useEffect, useState } from 'react';
import { fetchAnalyticsData } from '../api/analytics';

const AnalyticsReporting = () => {
  const [analyticsData, setAnalyticsData] = useState(null);

  useEffect(() => {
    const getAnalyticsData = async () => {
      const data = await fetchAnalyticsData();
      setAnalyticsData(data);
    };

    getAnalyticsData();
  }, []);

  if (!analyticsData) {
    return <div>Loading analytics data...</div>;
  }

  return (
    <div>
      <h2>Analytics and Reporting</h2>
      <div>
        <h3>Course Distribution</h3>
        <p>{analyticsData.courseDistribution}</p>
      </div>
      <div>
        <h3>Instructor Workload</h3>
        <p>{analyticsData.instructorWorkload}</p>
      </div>
      <div>
        <h3>Constraint Satisfaction</h3>
        <p>{analyticsData.constraintSatisfaction}</p>
      </div>
    </div>
  );
};

export default AnalyticsReporting;
