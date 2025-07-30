'use client'

import { useState } from 'react'
import Link from 'next/link'
import { FaPlus, FaFileAlt, FaClock, FaEdit, FaDownload, FaTrash } from 'react-icons/fa'
import { motion } from 'framer-motion'

export default function DashboardPage() {
  const [resumes, setResumes] = useState([
    {
      id: 1,
      title: 'Software Engineer Resume',
      template: 'Modern',
      lastModified: '2024-01-15',
      completeness: 85,
    },
    {
      id: 2,
      title: 'Product Manager Resume',
      template: 'Professional',
      lastModified: '2024-01-10',
      completeness: 100,
    },
  ])

  const handleDelete = (id: number) => {
    setResumes(resumes.filter(r => r.id !== id))
  }

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="flex justify-between items-center mb-8">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">My Resumes</h1>
            <p className="text-gray-600 mt-1">Create and manage your professional resumes</p>
          </div>
          <Link
            href="/builder/new"
            className="btn-primary inline-flex items-center gap-2"
          >
            <FaPlus /> Create New Resume
          </Link>
        </div>

        {/* Stats */}
        <div className="grid md:grid-cols-3 gap-6 mb-8">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="bg-white rounded-lg shadow p-6"
          >
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600">Total Resumes</p>
                <p className="text-2xl font-bold text-gray-900">{resumes.length}</p>
              </div>
              <FaFileAlt className="text-3xl text-primary-600" />
            </div>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
            className="bg-white rounded-lg shadow p-6"
          >
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600">Downloads</p>
                <p className="text-2xl font-bold text-gray-900">12</p>
              </div>
              <FaDownload className="text-3xl text-green-600" />
            </div>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
            className="bg-white rounded-lg shadow p-6"
          >
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600">Last Updated</p>
                <p className="text-2xl font-bold text-gray-900">Today</p>
              </div>
              <FaClock className="text-3xl text-purple-600" />
            </div>
          </motion.div>
        </div>

        {/* Resumes Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {resumes.map((resume, index) => (
            <motion.div
              key={resume.id}
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ delay: index * 0.1 }}
              className="bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow"
            >
              <div className="h-48 bg-gradient-to-br from-primary-100 to-purple-100 p-6">
                <div className="bg-white rounded-lg h-full shadow-md p-4">
                  <div className="h-2 bg-gray-200 rounded w-3/4 mb-2"></div>
                  <div className="h-2 bg-gray-200 rounded w-1/2 mb-4"></div>
                  <div className="space-y-1">
                    <div className="h-1 bg-gray-200 rounded"></div>
                    <div className="h-1 bg-gray-200 rounded"></div>
                    <div className="h-1 bg-gray-200 rounded w-5/6"></div>
                  </div>
                </div>
              </div>

              <div className="p-6">
                <h3 className="font-semibold text-lg text-gray-900 mb-2">
                  {resume.title}
                </h3>
                <p className="text-sm text-gray-600 mb-4">
                  Template: {resume.template}
                </p>

                <div className="mb-4">
                  <div className="flex justify-between text-sm mb-1">
                    <span className="text-gray-600">Completeness</span>
                    <span className="font-semibold">{resume.completeness}%</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div
                      className="bg-primary-600 h-2 rounded-full"
                      style={{ width: `${resume.completeness}%` }}
                    ></div>
                  </div>
                </div>

                <div className="flex items-center justify-between text-sm text-gray-600 mb-4">
                  <span className="flex items-center gap-1">
                    <FaClock /> {resume.lastModified}
                  </span>
                </div>

                <div className="flex gap-2">
                  <Link
                    href={`/builder/${resume.id}`}
                    className="flex-1 btn-primary text-sm py-2 text-center"
                  >
                    <FaEdit className="inline mr-1" /> Edit
                  </Link>
                  <button
                    onClick={() => handleDelete(resume.id)}
                    className="px-4 py-2 bg-red-100 text-red-600 rounded-lg hover:bg-red-200 transition-colors"
                  >
                    <FaTrash />
                  </button>
                </div>
              </div>
            </motion.div>
          ))}

          {/* Create New Card */}
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: resumes.length * 0.1 }}
          >
            <Link
              href="/builder/new"
              className="h-full min-h-[400px] bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow border-2 border-dashed border-gray-300 flex flex-col items-center justify-center text-gray-500 hover:text-primary-600 hover:border-primary-600 group"
            >
              <FaPlus className="text-5xl mb-4 group-hover:scale-110 transition-transform" />
              <p className="text-lg font-semibold">Create New Resume</p>
              <p className="text-sm mt-2">Start from scratch or use a template</p>
            </Link>
          </motion.div>
        </div>
      </div>
    </div>
  )
}