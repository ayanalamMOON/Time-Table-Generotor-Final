import React, { useEffect, useState } from 'react';
import { fetchAnalyticsData, exportAnalyticsReport } from '../api/analytics';
import { Button } from '@mui/material';
import { Bar, Pie } from 'react-chartjs-2';
import 'chart.js/auto';

const AnalyticsReporting = () => {
  const [analyticsData, setAnalyticsData] = useState(null);

  useEffect(() => {
    const getAnalyticsData = async () => {
      const data = await fetchAnalyticsData();
      setAnalyticsData(data);
    };

    getAnalyticsData();
  }, []);

  const handleExport = async (format) => {
    await exportAnalyticsReport(format);
  };

  if (!analyticsData) {
    return <div>Loading analytics data...</div>;
  }

  const courseDistributionData = {
    labels: Object.keys(analyticsData.courseDistribution),
    datasets: [
      {
        label: 'Course Distribution',
        data: Object.values(analyticsData.courseDistribution),
        backgroundColor: 'rgba(75, 192, 192, 0.6)',
      },
    ],
  };

  const instructorWorkloadData = {
    labels: Object.keys(analyticsData.instructorWorkload),
    datasets: [
      {
        label: 'Instructor Workload',
        data: Object.values(analyticsData.instructorWorkload),
        backgroundColor: 'rgba(153, 102, 255, 0.6)',
      },
    ],
  };

  const constraintSatisfactionData = {
    labels: ['Satisfied', 'Not Satisfied'],
    datasets: [
      {
        label: 'Constraint Satisfaction',
        data: [
          analyticsData.constraintSatisfaction * 100,
          (1 - analyticsData.constraintSatisfaction) * 100,
        ],
        backgroundColor: ['rgba(54, 162, 235, 0.6)', 'rgba(255, 99, 132, 0.6)'],
      },
    ],
  };

  return (
    <div>
      <h2>Analytics and Reporting</h2>
      <div>
        <h3>Course Distribution</h3>
        <Bar data={courseDistributionData} />
      </div>
      <div>
        <h3>Instructor Workload</h3>
        <Bar data={instructorWorkloadData} />
      </div>
      <div>
        <h3>Constraint Satisfaction</h3>
        <Pie data={constraintSatisfactionData} />
      </div>
      <Button variant="contained" color="primary" onClick={() => handleExport('pdf')}>
        Export as PDF
      </Button>
      <Button variant="contained" color="secondary" onClick={() => handleExport('excel')}>
        Export as Excel
      </Button>
    </div>
  );
};

export default AnalyticsReporting;
