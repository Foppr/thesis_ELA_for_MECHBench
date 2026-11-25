import numpy as np

class AdaptiveEllipticValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for elliptic valley structure with fractal-like properties
        self.valley_axes = np.logspace(0.5, 4.0, min(20, dim))
        self.conditioning_gradients = np.logspace(1.0, 7.0, min(15, dim))
        self.cross_dim_couplings = np.random.uniform(0.1, 5.0, min(25, dim))
        # Dynamic scaling factors that vary with dimension
        self.dynamic_scaling = np.random.lognormal(0.0, 0.9, min(12, dim))
        # Create adaptive noise parameters with fractal characteristics
        self.noise_levels = np.random.uniform(0.01, 1.0, min(10, dim))
        # Fractal sine-wave interaction parameters
        self.fractal_freqs = np.logspace(0.5, 3.5, min(15, dim))
        self.fractal_ampls = np.random.lognormal(0.0, 1.0, min(15, dim))
        # Multi-scale coupling strengths
        self.multi_scale_couplings = np.random.uniform(0.05, 2.0, min(20, dim))
        
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
            
        # Cross-dimensional coupling with multi-scale strengths
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                coupling_strength = self.cross_dim_couplings[(i + j) % len(self.cross_dim_couplings)]
                cross_term = coupling_strength * np.sin(x_norm[i] * x_norm[j])
                coupling_term += cross_term
                
        # Multi-scale fractal coupling
        fractal_term = 0.0
        for i in range(self.dim):
            scale_factor = self.multi_scale_couplings[i % len(self.multi_scale_couplings)]
            freq = self.fractal_freqs[i % len(self.fractal_freqs)]
            ampl = self.fractal_ampls[i % len(self.fractal_ampls)]
            fractal_term += scale_factor * ampl * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
            
        # Adaptive scaling based on dimension index
        scaling_term = 0.0
        for i in range(self.dim):
            scale_factor = self.dynamic_scaling[i % len(self.dynamic_scaling)]
            scaling_term += scale_factor * np.cos(2.0 * x_norm[i])
            
        # Dynamic conditioning gradient effects with fractal components
        gradient_term = 0.0
        for i in range(self.dim):
            grad_factor = self.conditioning_gradients[i % len(self.conditioning_gradients)]
            freq = self.fractal_freqs[i % len(self.fractal_freqs)]
            gradient_term += grad_factor * np.sin(1.5 * x_norm[i]) * np.cos(0.5 * x_norm[i]) + \
                           0.3 * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
            
        # Add noise component with varying intensity per dimension
        noise_term = 0.0
        for i in range(min(len(self.noise_levels), self.dim)):
            noise_level = self.noise_levels[i]
            noise_term += noise_level * np.random.normal(0.0, 1.0) * np.sin(5.0 * x_norm[i])
            
        # Combine all components with adaptive weights
        result = result + 0.8 * coupling_term + 0.6 * scaling_term + 0.4 * gradient_term + 0.2 * noise_term + 0.3 * fractal_term
        
        return result