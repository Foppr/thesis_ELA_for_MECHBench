import numpy as np

class QuaternionRadialSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize quaternion-inspired parameters
        self.quaternion_coeffs = np.random.rand(dim, 4) * 2 - 1
        self.radial_centers = np.random.rand(dim) * 10 - 5
        self.spectral_filters = np.random.rand(dim) * 0.5 + 0.5
        self.frequency_modulators = np.random.rand(dim) * 3 + 1
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Radial basis component with quaternion-inspired interactions
        radial_term = 0.0
        for i in range(self.dim):
            center = self.radial_centers[i]
            diff = x_normalized[i] - center
            radial_term += np.exp(-0.5 * (diff**2) / (0.1 + self.spectral_filters[i])) * \
                          np.cos(2 * np.pi * self.frequency_modulators[i] * diff)
        
        # Quaternion-inspired coupling between dimensions
        quaternion_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use quaternion-like interaction with normalized coefficients
                q_i = self.quaternion_coeffs[i]
                q_j = self.quaternion_coeffs[j]
                dot_product = np.dot(q_i, q_j)
                distance = np.abs(x_normalized[i] - x_normalized[j])
                quaternion_term += dot_product * np.sin(distance) * \
                                  np.exp(-0.1 * distance**2)
        
        # Adaptive spectral filtering component
        spectral_term = 0.0
        for i in range(self.dim):
            xi = x_normalized[i]
            # Apply frequency-dependent filtering with dynamic modulation
            freq_mod = self.frequency_modulators[i]
            spectral_term += np.sin(freq_mod * xi) * np.cos(freq_mod * xi) * \
                            np.exp(-0.5 * (xi**2) / (0.2 + self.spectral_filters[i]))
        
        # Cross-dimensional coupling with dynamic curvature
        curvature_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic curvature based on dimension interaction
                curv = np.sin(3 * (x_normalized[i] + x_normalized[j])) * \
                       np.cos(2 * (x_normalized[i] - x_normalized[j]))
                curvature_term += curv * np.exp(-0.3 * (x_normalized[i]**2 + x_normalized[j]**2))
        
        # Multi-scale oscillation component for enhanced multimodality
        oscillation_term = 0.0
        for i in range(self.dim):
            xi = x_normalized[i]
            # Combine multiple frequency oscillations with varying amplitudes
            oscillation_term += (np.sin(5 * xi) + 0.5 * np.sin(12 * xi) + 
                               0.3 * np.sin(20 * xi)) * \
                              np.exp(-0.2 * xi**2)
        
        # Global shaping component with adaptive scaling
        global_term = np.sum(np.abs(x_normalized)**3) * np.cos(np.sum(x_normalized))
        
        # Combine all terms with optimized weights for maximum multimodality
        return 0.25 * radial_term + 0.20 * quaternion_term + 0.15 * spectral_term + \
               0.15 * curvature_term + 0.10 * oscillation_term + 0.15 * global_term