from apscheduler.triggers.interval import IntervalTrigger

from cypherpunkpay.common import *
from test.unit.cypherpunkpay.cypherpunkpay_db_test_case import CypherpunkpayDBTestCase
from cypherpunkpay.jobs.job_scheduler import JobScheduler
from cypherpunkpay.usecases.report_jobs_uc import ReportJobsUC


def empty():
    pass


class ReportJobsUCTest(CypherpunkpayDBTestCase):

    def setUp(self):
        super().setUp()
        self.job_scheduler = JobScheduler()

    def tearDown(self):
        self.job_scheduler.shutdown()
        super().tearDown()

    def test_exec(self):
        self.job_scheduler.add_job(empty, id='refresh_job_rwer334', trigger=IntervalTrigger(minutes=2))
        self.job_scheduler.add_job(empty, id='refresh_job_3423ref', trigger=IntervalTrigger(seconds=2))
        self.job_scheduler.add_job(empty, id='refresh_job_gj3u4t9', trigger=IntervalTrigger(minutes=30))

        jobs = self.job_scheduler.get_all_jobs()

        report = ReportJobsUC(self.job_scheduler).exec()

        # total
        self.assertEqual(3, report.total)

        # jobs_by_next_run
        self.assertEqual('refresh_job_3423ref', report.jobs_by_next_run[0].id)
        self.assertEqual('refresh_job_rwer334', report.jobs_by_next_run[1].id)
        self.assertEqual('refresh_job_gj3u4t9', report.jobs_by_next_run[2].id)

        # jobs_scheduled_until
        count = report.jobs_scheduled_until(utc_from_now(seconds=11))
        self.assertEqual(5, count)
