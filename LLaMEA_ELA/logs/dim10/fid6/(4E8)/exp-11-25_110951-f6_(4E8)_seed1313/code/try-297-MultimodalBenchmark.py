import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic coupling with modified exponential potentials
        chaotic_coupling = 0.0
        for i in range(self.dim):
            chaotic_coupling += np.exp(-0.5 * (x_norm[i] - np.sin(x_norm[i]))**2) * \
                               np.sin(10 * x_norm[i]) * np.cos(8 * x_norm[i])
        
        # Logarithmic barrier potentials with dynamic scaling
        log_barrier = 0.0
        for i in range(self.dim):
            log_barrier += (np.log(1 + 0.5 * (x_norm[i] - 1)**2) +
                           0.7 * np.log(1 + 0.3 * (x_norm[i] + 1)**2) +
                           0.4 * np.log(1 + 0.2 * x_norm[i]**2))
        
        # Spectral harmonic interference with asymmetric elliptic structures
        spectral_harmonic = 0.0
        for i in range(self.dim):
            spectral_harmonic += (np.sin(20 * x_norm[i]) * np.cos(18 * x_norm[i]) +
                                0.6 * np.sin(15 * x_norm[i])**3 * np.cos(12 * x_norm[i]))
        
        # Modified exponential potentials with cross-dimensional interactions
        cross_interaction = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            cross_interaction += np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * \
                               (np.sin(2 * x_norm[i]) * np.cos(2 * x_norm[j]) +
                                0.5 * np.sin(3 * x_norm[i]) * np.cos(3 * x_norm[j]))
        
        # Fractal-like self-similarity with log-periodic oscillations
        fractal_log_osc = 0.0
        for i in range(self.dim):
            freq = 1 + 0.5 * np.sin(x_norm[i])
            fractal_log_osc += (np.sin(freq * 10 * x_norm[i]) * np.cos(freq * 8 * x_norm[i]) +
                              0.3 * np.sin(freq * 15 * x_norm[i])**2 * np.cos(freq * 12 * x_norm[i]))
        
        # Multi-scale sinusoidal modulations with dynamic weighting
        multi_scale = 0.0
        scales = [2, 3, 5, 7, 11]
        for i in range(self.dim):
            for s in scales:
                multi_scale += np.sin(s * x_norm[i]) * np.cos(s * x_norm[i] / (s + 1)) * \
                              np.exp(-0.1 * (x_norm[i] - np.sin(x_norm[i]))**2)
        
        # Asymmetric elliptic structures with enhanced gradient coupling
        elliptic_structure = 0.0
        for i in range(self.dim):
            elliptic_structure += (np.sin(5 * x_norm[i]) * np.cos(4 * x_norm[i]) +
                                0.3 * np.sin(8 * x_norm[i])**2 * np.cos(6 * x_norm[i]))
        
        # Adjusted spectral interference terms for better benchmark differentiation
        spectral_interference = 0.0
        for i in range(self.dim):
            spectral_interference += (np.sin(12 * x_norm[i]) * np.cos(10 * x_norm[i]) +
                                   0.4 * np.sin(9 * x_norm[i])**2 * np.cos(7 * x_norm[i]))
        
        # Dynamic gradient coupling with probabilistic basin attraction
        gradient_coupling = 0.0
        for i in range(self.dim):
            gradient_coupling += (0.5 * np.sin(6 * x_norm[i]) * np.cos(5 * x_norm[i]) +
                                0.3 * np.sin(4 * x_norm[i])**2 * np.cos(3 * x_norm[i]))
        
        # Combine all components with optimized weights
        return (0.2 * chaotic_coupling + 0.15 * log_barrier + 0.15 * spectral_harmonic + 
                0.1 * cross_interaction + 0.1 * fractal_log_osc + 0.1 * multi_scale + 
                0.08 * elliptic_structure + 0.07 * spectral_interference + 0.05 * gradient_coupling)