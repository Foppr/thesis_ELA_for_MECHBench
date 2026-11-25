import numpy as np

class ChaoticEllipticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic coupling parameters with fractal characteristics
        self.fractal_params = np.logspace(0.5, 2.5, min(10, dim)) * 1.5
        # Dynamic conditioning gradients with elliptic curvature modulation
        self.conditioning_gradients = np.linspace(1.0, 4.0, min(12, dim)) * 1.3
        # Cross-dimensional interaction patterns with phase coupling
        self.interaction_params = np.random.uniform(0.8, 2.5, min(9, dim)) * 1.4
        # Fractal sine-wave interaction parameters for increased multimodality
        self.fractal_sine_params = np.logspace(1.0, 3.0, min(8, dim)) * 0.7
        # Hyperbolic tangent modulation for enhanced nonlinearity
        self.tanh_params = np.random.uniform(0.5, 2.0, min(7, dim)) * 1.2
        # Adaptive scaling factors based on dimensionality
        self.adaptive_scale = 1.0 + 0.1 * np.log10(dim + 1)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Enhanced chaotic coupling with fractal sine-wave interactions
        chaotic_term = 0.0
        for i in range(min(len(self.fractal_params), self.dim)):
            fractal_val = self.fractal_params[i] * np.sin(self.fractal_sine_params[i] * x_norm[i])
            chaotic_term += fractal_val
            
        # Dynamic conditioning gradients with elliptic curvature and exponential modulation
        conditioning_term = 0.0
        for i in range(min(len(self.conditioning_gradients), self.dim)):
            gradient = self.conditioning_gradients[i]
            # Enhanced conditioning with elliptic curvature, cubic modulation and hyperbolic tangent
            cond_val = gradient * np.exp(0.3 * x_norm[i] ** 2) + 0.5 * (x_norm[i] ** 3) + 0.2 * (x_norm[i] ** 5)
            cond_val += self.tanh_params[i % len(self.tanh_params)] * np.tanh(2.0 * x_norm[i])
            conditioning_term += cond_val
            
        # Cross-dimensional interference with chaotic coupling strength and phase modulation
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Interference with chaotic coupling strength and phase modulation
                coupling_strength = self.interaction_params[i % len(self.interaction_params)]
                phase_shift = np.pi * (i + j) / (self.dim + 2)
                interference_val = coupling_strength * x_norm[i] * x_norm[j] * np.sin(phase_shift + 3.0 * x_norm[i] + 0.5 * x_norm[j])
                interference_term += interference_val
                
        # Fractal multi-scale clustering with varying separation distances
        cluster_term = 0.0
        for i in range(self.dim):
            # Cluster positioning with fractal spacing and sinusoidal modulation
            cluster_pos = 2.0 * np.sin(0.7 * (i + 1) * np.pi / self.dim) + 0.5 * np.cos(1.3 * (i + 1) * np.pi / self.dim)
            distance = x_norm[i] - cluster_pos
            # Fractal clustering with increasing polynomial orders and chaotic scaling
            cluster_val = 1.5 * (distance ** 3) + 0.8 * (distance ** 5) + 0.3 * (distance ** 7) + 0.1 * (distance ** 9) + 0.05 * (distance ** 11)
            cluster_term += cluster_val
            
        # Additional chaotic noise with dimensionality-dependent amplitude
        noise_amplitude = 0.05 * (1.0 + 0.1 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        # Combined terms with adjusted weights for extreme landscape characteristics
        result = 1.3 * chaotic_term + 1.0 * conditioning_term + 0.8 * interference_term + 0.7 * cluster_term
        
        # Apply adaptive scaling factor to the final result
        result *= self.adaptive_scale
        
        return result + noise