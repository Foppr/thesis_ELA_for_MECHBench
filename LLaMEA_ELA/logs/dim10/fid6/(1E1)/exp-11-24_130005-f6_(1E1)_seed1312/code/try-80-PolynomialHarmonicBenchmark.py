import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial barrier terms with varying degrees and positions
        poly_barrier = 0.0
        for i in range(self.dim):
            # Create multiple polynomial barriers with different strengths
            poly_barrier += (x_scaled[i]**4 - 2.0 * x_scaled[i]**2 + 1.0) * \
                           np.exp(-0.5 * (x_scaled[i] - 0.5)**2) + \
                           (x_scaled[i]**6 - 3.0 * x_scaled[i]**4 + 3.0 * x_scaled[i]**2) * \
                           np.exp(-0.3 * (x_scaled[i] + 0.3)**2)
        
        # Radial basis function component with multiple centers
        rbf_term = 0.0
        centers = np.linspace(-0.8, 0.8, min(5, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                rbf_term += np.exp(-10.0 * (x_scaled[i] - centers[i])**2)
        
        # Coupled harmonic oscillators with frequency modulation
        harmonic_term = 0.0
        for i in range(self.dim):
            freq_i = 1.0 + 0.5 * np.sin(x_scaled[i])
            harmonic_term += freq_i * np.sin(freq_i * x_scaled[i]) * \
                           np.cos(0.5 * x_scaled[i])
        
        # Cross-dimensional coupling with varying interaction strengths
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                strength = 0.3 + 0.2 * np.sin(x_scaled[i] + x_scaled[j])
                cross_coupling += strength * np.sin(2.0 * x_scaled[i]) * \
                                np.cos(1.5 * x_scaled[j]) * \
                                np.exp(-0.1 * (x_scaled[i] - x_scaled[j])**2)
        
        # Multimodal sine-wave component with varying amplitudes
        sine_component = 0.0
        for i in range(self.dim):
            amplitude = 0.5 + 0.3 * np.sin(2.0 * x_scaled[i])
            sine_component += amplitude * np.sin(8.0 * x_scaled[i]) + \
                            0.4 * np.sin(12.0 * x_scaled[i]) + \
                            0.2 * np.sin(16.0 * x_scaled[i])
        
        # Global scaling and combination
        return 1.2 * poly_barrier + 0.8 * rbf_term + 0.9 * harmonic_term + \
               0.7 * cross_coupling + 0.6 * sine_component + 1.5