import numpy as np

class ChaoticSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine-wave interaction with modified logistic map
        chaotic_term = 0.0
        r = 3.8  # Slightly reduced chaos for better control
        for i in range(self.dim):
            if i == 0:
                xi_prev = x[-1] if self.dim > 1 else 0
            else:
                xi_prev = x[i-1]
            chaotic_term += np.sin(r * xi_prev * (1 - xi_prev)) * np.sin(2.0 * x[i])
        chaotic_term /= self.dim
        
        # Modified adaptive conditioning with dynamic scaling
        cond_scale = 1.0 + 0.3 * np.std(x) + 0.2 * np.mean(np.abs(x))
        adaptive_term = np.sum((x**2) * np.cos(4.0 * x) * cond_scale) / (self.dim * 2.5)
        
        # Strengthened cross-dimensional coupling with hyperbolic interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.tanh(0.5 * (x[i] - x[j])) * np.sinh(x[i] + x[j])
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Enhanced multi-modal structure with composite sinusoidal basins
        modal_term = np.sum(np.sin(3.0 * np.pi * x) * np.cos(0.7 * np.pi * x) + 
                           0.5 * np.sin(6.0 * np.pi * x)) / self.dim
        
        # Improved noise injection with frequency modulation
        noise_amp = 0.15 + 0.08 * np.mean(np.abs(x))
        noise_term = np.sum(noise_amp * np.sin(x * np.pi * (1.0 + 0.2 * np.sin(0.5 * x)))) / self.dim
        
        # Refined polynomial distortion with asymmetric higher-order terms
        poly_term = np.sum(0.3 * x**5 - 1.8 * x**4 + 2.7 * x**3 - 1.2 * x**2) / self.dim
        
        # Combine all terms with adjusted weights for better balance
        total = 0.25 * chaotic_term + 0.22 * adaptive_term + 0.20 * cross_term + 0.15 * modal_term + 0.10 * noise_term + 0.08 * poly_term
        
        return total