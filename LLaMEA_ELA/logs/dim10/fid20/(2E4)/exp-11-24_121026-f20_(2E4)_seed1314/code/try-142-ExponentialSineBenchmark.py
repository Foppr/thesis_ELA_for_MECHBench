import numpy as np

class ExponentialSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Exponential decay potentials with varying scales
        exp_potentials = []
        for i in range(self.dim):
            scale = 0.5 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            exp_potentials.append(np.exp(-scale * np.abs(x_norm[i])) * 
                                np.cos(3 * x_norm[i])**2)
        
        # Sine-wave coupling between dimensions
        sine_coupling = 0.0
        for i in range(self.dim - 1):
            sine_coupling += np.sin(7 * x_norm[i] + 5 * x_norm[i+1]) * \
                           np.cos(4 * x_norm[i] - 6 * x_norm[i+1])
        
        # Adaptive dimensional scaling based on position
        adaptive_scale = 0.0
        for i in range(self.dim):
            adaptive_scale += (1 + 0.3 * np.sin(2 * x_norm[i])) * x_norm[i]**2
        
        # Multi-scale harmonic components with frequency modulation
        harmonic_components = 0.0
        frequencies = [2, 4, 6, 8]
        for freq in frequencies:
            harmonic_components += np.sum(np.sin(freq * x_norm + 
                                              np.sin(freq**2 * x_norm))**2)
        
        # Quadratic basin with exponential barriers
        quadratic_basin = np.sum(x_norm**2)
        barrier_terms = 0.0
        for i in range(self.dim):
            barrier_terms += np.exp(2 * (1 - np.abs(x_norm[i]))**2) if np.abs(x_norm[i]) < 1 else 0
        
        # Combine all components with dynamic weighting
        return (0.6 * np.sum(exp_potentials) + 0.3 * sine_coupling + 
                0.2 * adaptive_scale + 0.15 * harmonic_components + 
                0.1 * quadratic_basin + 0.05 * barrier_terms)