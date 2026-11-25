import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced logarithmic repulsion with adaptive strength
        log_repulsion = np.sum(0.4 * np.log(1.0 + 0.3 * np.abs(x_scaled) + 0.05 * x_scaled**2))
        
        # Refined chaotic gradient modulation with frequency modulation
        chaotic_grad = np.sum(np.sin(17 * x_scaled) * np.cos(11 * x_scaled) * 
                              (1.0 + 0.3 * np.sin(5 * x_scaled**2) + 0.2 * np.cos(9 * x_scaled)))
        
        # Improved multi-scale harmonic interference with dynamic amplitudes
        harmonic_interference = 0.0
        for i in range(1, 7):
            amplitude = 1.0 / (1.0 + 0.1 * i)
            harmonic_interference += np.sum(amplitude * np.sin(i * x_scaled) * np.cos(i * x_scaled**3) * 
                                          (1.0 + 0.15 * np.sin(i * self.dim + 0.5 * x_scaled.sum())))
        
        # Enhanced saddle-point attraction with dynamic phase and strength
        saddle_attraction = np.sum(0.6 * (x_scaled**2 - 1.0)**2 * 
                                  (1.0 + 0.25 * np.cos(4 * x_scaled) + 0.1 * np.sin(2 * x_scaled**2)))
        
        # Improved cross-dimensional coupling with cosine modulation
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = np.exp(-0.3 * (x_scaled[i] - x_scaled[j])**2) * \
                                   (1.0 + 0.1 * np.cos(3 * (x_scaled[i] + x_scaled[j])))
                cross_coupling += coupling_strength * np.sin(5 * (x_scaled[i] + x_scaled[j]))
        
        # Enhanced conditioning factor with dimensionality-dependent scaling
        condition_factor = 1.0 + 0.15 * np.log(self.dim + 1) + 0.02 * np.sin(self.dim * 0.5)
        
        # Combine all components with refined weights
        return condition_factor * (1.8 * log_repulsion + 1.7 * chaotic_grad + 
                                  0.9 * harmonic_interference + 1.3 * saddle_attraction + 
                                  0.7 * cross_coupling)