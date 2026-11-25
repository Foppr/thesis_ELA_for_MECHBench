import numpy as np

class FractalQuantumGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters
        self.hurst = 0.3
        self.fractal_scale = 1.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal Brownian motion component with enhanced complexity
        fbm_sum = 0.0
        for i in range(self.dim):
            # Enhanced fractal-like behavior using higher-order sine and cosine combinations
            fbm_sum += (np.sin(x[i]) * np.cos(2 * x[i]) + 
                       0.5 * np.sin(3 * x[i]) * np.cos(4 * x[i]) +
                       0.3 * np.sin(5 * x[i]) * np.cos(6 * x[i]) +
                       0.1 * np.sin(7 * x[i]) * np.cos(8 * x[i]) +
                       0.2 * np.sin(9 * x[i]) * np.cos(10 * x[i]))
        
        # Quantum harmonic oscillator component with enhanced nonlinearity
        quantum_sum = 0.0
        for i in range(self.dim):
            # Harmonic oscillator potential with quantum-like modulation and additional terms
            omega = 1.0 + 0.3 * np.sin(x[i]) + 0.1 * np.cos(2 * x[i])
            quantum_sum += 0.5 * omega**2 * x[i]**2 + 0.5 * (1 + 0.4 * np.cos(x[i])) + \
                          0.05 * np.sin(3 * x[i]) * x[i]**3
        
        # Adaptive gradient field component with enhanced complexity
        grad_sum = 0.0
        for i in range(self.dim):
            # Gradient field with adaptive strength based on position and higher-order terms
            strength = 1.0 + 0.6 * np.sin(0.5 * x[i]) + 0.2 * np.cos(0.3 * x[i])
            grad_sum += strength * (x[i]**4 - 3*x[i]**3 + 2*x[i]**2 - x[i])
        
        # Multi-scale interference patterns with increased complexity and modified interaction
        interference_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction range
                freq_i = 1.0 + 0.5 * np.sin(x[i]) + 0.2 * np.cos(2 * x[i])  # Enhanced frequency modulation
                freq_j = 1.0 + 0.5 * np.cos(x[j]) + 0.2 * np.sin(2 * x[j])  # Enhanced frequency modulation
                interference_sum += np.sin(freq_i * x[i]) * np.cos(freq_j * x[j]) * \
                                  np.exp(-0.2 * (x[i] - x[j])**2)  # Increased decay rate
        
        # Boundary attraction and repulsion with enhanced dynamics
        boundary_sum = 0.0
        for i in range(self.dim):
            # Attract towards center, repel from boundaries with different strengths and enhanced modulation
            if x[i] < 0:
                boundary_sum += 3.0 * np.exp(-0.25 * (x[i] + 5.0)**2) * (1 + 0.3 * np.sin(4 * x[i]) + 0.1 * np.cos(2 * x[i]))
            else:
                boundary_sum += 2.0 * np.exp(-0.35 * (x[i] - 5.0)**2) * (1 + 0.2 * np.cos(3 * x[i]) + 0.1 * np.sin(2 * x[i]))
        
        # Chaotic modulation with logistic map and enhanced complexity
        chaotic_sum = 0.0
        r = 4.0  # Increased chaotic parameter for more complexity
        for i in range(self.dim):
            logistic_val = r * (x[i] / 5.0) * (1 - x[i] / 5.0)
            chaotic_sum += 0.7 * logistic_val**3 + 0.3 * logistic_val**2  # Enhanced chaotic contribution
        
        # Multi-modal Gaussian components with dynamic centers, widths, and enhanced interaction
        gaussian_sum = 0.0
        for i in range(self.dim):
            center = 2.5 * np.sin(x[i]) + 0.5 * np.cos(2 * x[i])  # Enhanced dynamic center
            width = 0.9 + 0.5 * np.cos(x[i]) + 0.1 * np.sin(2 * x[i])  # Enhanced dynamic width
            gaussian_sum += 2.0 * np.exp(-0.5 * ((x[i] - center) / width)**2) + \
                           0.5 * np.sin(3 * x[i]) * np.cos(4 * x[i])  # Increased amplitude and added interaction
        
        # Additional complex interaction terms
        interaction_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+2, self.dim)):
                interaction_sum += 0.3 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * \
                                  np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Final combined function
        result = fbm_sum + quantum_sum + grad_sum + interference_sum + boundary_sum + \
                 chaotic_sum + gaussian_sum + interaction_sum
        
        return result