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
        
        # Fractal Brownian motion component with higher dimensionality interaction
        fbm_sum = 0.0
        for i in range(self.dim):
            # Enhanced fractal behavior using multiple sine/cosine combinations
            fbm_sum += (np.sin(x[i]) * np.cos(2 * x[i]) + 
                       0.5 * np.sin(3 * x[i]) * np.cos(4 * x[i]) +
                       0.3 * np.sin(5 * x[i]) * np.cos(6 * x[i]) +
                       0.1 * np.sin(7 * x[i]) * np.cos(8 * x[i]))
        
        # Quantum harmonic oscillator component with dynamic coupling
        quantum_sum = 0.0
        for i in range(self.dim):
            # Harmonic oscillator potential with quantum-like modulation and coupling
            omega = 1.0 + 0.3 * np.sin(x[i]) + 0.2 * np.cos(2 * x[i])
            quantum_sum += 0.5 * omega**2 * x[i]**2 + 0.5 * (1 + 0.4 * np.cos(x[i])) + \
                          0.1 * np.sin(x[i]) * np.cos(2 * x[i]) * x[i]
        
        # Adaptive gradient field component with multi-scale influence
        grad_sum = 0.0
        for i in range(self.dim):
            # Gradient field with adaptive strength based on position and neighborhood
            strength = 1.0 + 0.6 * np.sin(0.5 * x[i]) + 0.3 * np.cos(0.3 * x[i])
            grad_sum += strength * (x[i]**4 - 3*x[i]**3 + 2*x[i]**2 - x[i])
        
        # Multi-scale interference patterns with dynamic frequencies
        interference_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased interaction range
                freq_i = 1.0 + 0.4 * np.sin(x[i]) + 0.2 * np.cos(2 * x[i])
                freq_j = 1.0 + 0.4 * np.cos(x[j]) + 0.2 * np.sin(2 * x[j])
                interference_sum += np.sin(freq_i * x[i]) * np.cos(freq_j * x[j]) * \
                                  np.exp(-0.15 * (x[i] - x[j])**2) * \
                                  (1 + 0.3 * np.sin(0.5 * (x[i] + x[j])))
        
        # Enhanced boundary attraction and repulsion with multi-modal behavior
        boundary_sum = 0.0
        for i in range(self.dim):
            # Attract towards center, repel from boundaries with different strengths
            if x[i] < -2:
                boundary_sum += 3.0 * np.exp(-0.15 * (x[i] + 5.0)**2) * (1 + 0.3 * np.sin(4 * x[i]))
            elif x[i] > 2:
                boundary_sum += 2.5 * np.exp(-0.25 * (x[i] - 5.0)**2) * (1 + 0.2 * np.cos(3 * x[i]))
            else:
                boundary_sum += 1.0 * np.exp(-0.1 * (x[i])**2) * (1 + 0.1 * np.sin(2 * x[i]))
        
        # Chaotic modulation with logistic map and neural network-like behavior
        chaotic_sum = 0.0
        r = 3.9  # Increased chaos parameter
        for i in range(self.dim):
            logistic_val = r * (x[i] / 5.0) * (1 - x[i] / 5.0)
            chaotic_sum += 0.5 * logistic_val**2 + 0.2 * np.sin(logistic_val * 3)
        
        # Multi-modal Gaussian components with dynamic centers, widths, and amplitudes
        gaussian_sum = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(x[i]) + 0.5 * np.cos(2 * x[i])
            width = 0.8 + 0.4 * np.cos(x[i]) + 0.2 * np.sin(2 * x[i])
            amplitude = 1.5 + 0.5 * np.sin(3 * x[i])
            gaussian_sum += amplitude * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Additional neural network-inspired component with phase interference
        nn_sum = 0.0
        for i in range(self.dim):
            # Neural-like activation with phase modulation
            phase = 0.5 * np.sin(x[i]) + 0.3 * np.cos(2 * x[i])
            nn_sum += (0.8 * np.tanh(x[i]) + 0.3 * np.sin(3 * x[i]) * np.cos(phase)) * \
                     (1 + 0.2 * np.sin(0.5 * x[i]))
        
        # Final combined function
        result = fbm_sum + quantum_sum + grad_sum + interference_sum + boundary_sum + \
                 chaotic_sum + gaussian_sum + nn_sum
        
        return result