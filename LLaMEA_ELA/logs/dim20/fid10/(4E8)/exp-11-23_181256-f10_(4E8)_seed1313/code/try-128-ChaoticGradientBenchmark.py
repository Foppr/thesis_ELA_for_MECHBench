import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Logarithmic repulsion field with dynamic strength
        log_repulsion = np.sum(0.3 * np.log(1.0 + 0.5 * np.abs(x_scaled) + 0.1 * x_scaled**2))
        
        # Chaotic gradient modulation using sine-cosine coupling
        chaotic_grad = np.sum(np.sin(15 * x_scaled) * np.cos(13 * x_scaled) * 
                              (1.0 + 0.4 * np.sin(7 * x_scaled**2)))
        
        # Multi-scale harmonic interference with varying amplitudes
        harmonic_interference = 0.0
        for i in range(1, 6):
            harmonic_interference += np.sum(np.sin(i * x_scaled) * np.cos(i * x_scaled**3) * 
                                          (1.0 + 0.2 * np.sin(i * self.dim)))
        
        # Saddle-point attraction with variable strength and phase
        saddle_attraction = np.sum(0.5 * (x_scaled**2 - 1.0)**2 * 
                                  (1.0 + 0.3 * np.cos(3 * x_scaled)))
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.exp(-0.5 * (x_scaled[i] - x_scaled[j])**2) * \
                                 np.sin(4 * (x_scaled[i] + x_scaled[j]))
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Combine all components with adaptive weights
        return condition_factor * (2.0 * log_repulsion + 1.5 * chaotic_grad + 
                                  0.8 * harmonic_interference + 1.2 * saddle_attraction + 
                                  0.6 * cross_coupling)