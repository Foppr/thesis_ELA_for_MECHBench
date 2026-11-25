import numpy as np

class QuaternionRadialSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize quaternion-inspired parameters
        self.quaternion_coeffs = np.random.rand(dim, 4) * 2.0 - 1.0
        self.frequency_modulators = 1.0 + 0.5 * np.sin(np.arange(dim) * np.pi / (dim + 1))
        self.radial_centers = np.random.rand(dim) * 10.0 - 5.0
        self.spectral_weights = np.random.rand(dim) * 0.5 + 0.5
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_normalized = x / 5.0
        
        # Radial basis function component with quaternion-inspired coupling
        radial_term = 0.0
        for i in range(self.dim):
            xi = x_normalized[i]
            center = self.radial_centers[i]
            # Quaternion-inspired radial distance with multiple components
            dist = np.sqrt(np.sum((x_normalized - center)**2))
            radial_term += np.exp(-dist**2) * np.sin(self.spectral_weights[i] * dist)
        
        # Quaternion-inspired coupling component
        quaternion_term = 0.0
        for i in range(self.dim):
            xi = x_normalized[i]
            q_coeffs = self.quaternion_coeffs[i]
            # Combine multiple quaternion-like components
            quat_component = (q_coeffs[0] * np.sin(xi) + 
                            q_coeffs[1] * np.cos(xi) + 
                            q_coeffs[2] * np.tan(xi) + 
                            q_coeffs[3] * np.exp(-xi**2))
            quaternion_term += quat_component
        
        # Adaptive spectral decomposition component
        spectral_term = 0.0
        for i in range(self.dim):
            xi = x_normalized[i]
            freq_mod = self.frequency_modulators[i]
            # Multiple harmonic components with adaptive frequencies
            spectral_term += (np.sin(freq_mod * xi) * np.cos(freq_mod * xi) + 
                            np.sin(2 * freq_mod * xi) * np.cos(2 * freq_mod * xi))
        
        # Cross-dimensional interaction with spectral coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Spectral coupling between dimensions
                cross_term += (np.sin(self.frequency_modulators[i] * x_normalized[j]) * 
                             np.cos(self.frequency_modulators[j] * x_normalized[i]))
        
        # Non-linear frequency modulation component
        modulation_term = 0.0
        for i in range(self.dim):
            xi = x_normalized[i]
            # Adaptive frequency modulation based on position
            adaptive_freq = 5.0 + 3.0 * np.sin(xi)
            modulation_term += np.sin(adaptive_freq * xi) * np.cos(adaptive_freq * xi) * \
                              np.exp(-0.5 * xi**2)
        
        # Multi-scale oscillation component
        multi_scale_term = 0.0
        for i in range(self.dim):
            xi = x_normalized[i]
            # Multiple frequency scales with different amplitudes
            scales = [1.0, 2.0, 3.0, 5.0]
            for scale in scales:
                multi_scale_term += np.sin(scale * xi) * np.cos(scale * xi) * \
                                  np.exp(-0.1 * (scale * xi)**2)
        
        # Combine all components with carefully tuned weights
        return 0.25 * radial_term + 0.20 * quaternion_term + 0.18 * spectral_term + \
               0.15 * cross_term + 0.10 * modulation_term + 0.12 * multi_scale_term