import numpy as np

class AdaptiveEllipticValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for elliptic valley structure
        self.valley_axes = np.logspace(0.5, 3.0, min(15, dim))
        self.conditioning_gradients = np.logspace(1.0, 6.0, min(12, dim))
        self.cross_dim_couplings = np.random.uniform(0.5, 4.0, min(18, dim))  # Slightly increased range
        # Dynamic scaling factors that vary with dimension
        self.dynamic_scaling = np.random.lognormal(0.0, 0.7, min(10, dim))
        # Create adaptive noise parameters
        self.noise_levels = np.random.uniform(0.01, 0.5, min(8, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Initialize result
        result = 0.0
        
        # Elliptic valley components with adaptive axes and conditioning
        for i in range(self.dim):
            axis = self.valley_axes[i % len(self.valley_axes)]
            cond_grad = self.conditioning_gradients[i % len(self.conditioning_gradients)]
            
            # Elliptic valley term with dynamic conditioning
            valley_term = (x_norm[i] ** 2) / (axis + 1e-8)
            result += cond_grad * valley_term
            
        # Cross-dimensional coupling with dynamic strengths
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                coupling_strength = self.cross_dim_couplings[(i + j) % len(self.cross_dim_couplings)]
                cross_term = coupling_strength * np.sin(x_norm[i] * x_norm[j]) * np.cos(0.3 * (x_norm[i] + x_norm[j]))
                coupling_term += cross_term
                
        # Adaptive scaling based on dimension index
        scaling_term = 0.0
        for i in range(self.dim):
            scale_factor = self.dynamic_scaling[i % len(self.dynamic_scaling)]
            scaling_term += scale_factor * np.cos(2.0 * x_norm[i])
            
        # Dynamic conditioning gradient effects
        gradient_term = 0.0
        for i in range(self.dim):
            grad_factor = self.conditioning_gradients[i % len(self.conditioning_gradients)]
            gradient_term += grad_factor * np.sin(1.5 * x_norm[i]) * np.cos(0.5 * x_norm[i])
            
        # Add noise component with varying intensity per dimension
        noise_term = 0.0
        for i in range(min(len(self.noise_levels), self.dim)):
            noise_level = self.noise_levels[i]
            noise_term += noise_level * np.random.normal(0.0, 1.0) * np.sin(5.0 * x_norm[i])
            
        # Add sinusoidal modulation to increase multimodality
        mod_term = 0.0
        for i in range(self.dim):
            mod_term += 0.3 * np.sin(3.0 * x_norm[i]) * np.cos(1.2 * x_norm[i])
            
        # Combine all components with adaptive weights
        result = result + 0.8 * coupling_term + 0.6 * scaling_term + 0.4 * gradient_term + 0.2 * noise_term + 0.5 * mod_term
        
        return result