import numpy as np

class GaborWaveletBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize Gabor wavelet parameters
        self.center_frequencies = np.random.uniform(0.5, 3.0, dim)
        self.bandwidths = np.random.uniform(0.1, 1.5, dim)
        self.modulation_rates = np.random.uniform(0.2, 2.0, dim)
        self.interference_strengths = np.random.uniform(0.5, 2.5, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.spatial_scales = np.random.uniform(0.5, 3.0, dim)
        # Cross-dimensional coupling matrix
        self.coupling_matrix = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Adaptive frequency modulation parameters
        self.frequency_modulation_amplitudes = np.random.uniform(0.1, 1.0, dim)
        self.frequency_modulation_rates = np.random.uniform(0.1, 0.8, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            # Base Gabor wavelet component
            gabor_real = np.exp(-0.5 * (x_norm[i] / self.bandwidths[i])**2) * \
                        np.cos(self.center_frequencies[i] * x_norm[i] + self.phase_shifts[i])
            
            gabor_imag = np.exp(-0.5 * (x_norm[i] / self.bandwidths[i])**2) * \
                        np.sin(self.center_frequencies[i] * x_norm[i] + self.phase_shifts[i])
            
            # Adaptive frequency modulation
            adaptive_freq = self.center_frequencies[i] * (1.0 + self.frequency_modulation_amplitudes[i] * 
                                                          np.sin(self.frequency_modulation_rates[i] * x_norm[i]))
            
            modulated_component = np.exp(-0.5 * (x_norm[i] / self.bandwidths[i])**2) * \
                                np.cos(adaptive_freq * x_norm[i] + self.phase_shifts[i])
            
            # Spatial scaling and interference
            spatial_scaled = gabor_real * self.spatial_scales[i]
            interference = 0.0
            
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_matrix[i, j]
                    interference += coupling * np.sin(self.interference_strengths[j] * (x_norm[i] - x_norm[j]))
            
            # Combine components with interference
            wavelet_value = spatial_scaled + modulated_component + interference
            
            result += wavelet_value * np.exp(-0.2 * x_norm[i]**2)
        
        # Cross-dimensional interference patterns
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = self.coupling_matrix[i, j]
                cross_terms += coupling * np.sin(2.0 * (x_norm[i] - x_norm[j])) * \
                              np.cos(3.0 * (x_norm[i] + x_norm[j]))
        
        # Add global harmonic modulation
        global_modulation = np.sin(0.5 * np.sum(x_norm**2)) * np.cos(0.3 * np.sum(x_norm))
        
        # Final combination with adaptive weights
        total = 0.4 * result + 0.3 * cross_terms + 0.3 * global_modulation
        
        return total * (1.0 + 0.1 * np.sin(np.sum(x_norm**3) * 0.2))