import numpy as np

class ChaoticFractalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute multiple chaotic parameters for each dimension
        self.chaos_params1 = 3.9 + 0.2 * np.random.rand(dim)
        self.chaos_params2 = 3.5 + 0.3 * np.random.rand(dim)
        self.chaos_params3 = 4.0 + 0.1 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Multi-chaos component with three different chaotic maps
        chaos_sum = 0.0
        for i in range(self.dim):
            # First chaotic sequence
            x_chaos1 = 0.5 + 0.1 * np.random.rand()
            for _ in range(20):
                x_chaos1 = self.chaos_params1[i] * x_chaos1 * (1 - x_chaos1)
            
            # Second chaotic sequence
            x_chaos2 = 0.3 + 0.2 * np.random.rand()
            for _ in range(15):
                x_chaos2 = self.chaos_params2[i] * x_chaos2 * (1 - x_chaos2)
                
            # Third chaotic sequence
            x_chaos3 = 0.7 + 0.1 * np.random.rand()
            for _ in range(25):
                x_chaos3 = self.chaos_params3[i] * x_chaos3 * (1 - x_chaos3)
            
            chaos_sum += (x_chaos1 * np.sin(x_norm[i] * np.pi) + 
                         x_chaos2 * np.cos(x_norm[i] * 0.5) + 
                         x_chaos3 * np.tan(x_norm[i] * 0.3)) * 0.33
        
        # Multi-fractal noise component with varying fractal dimensions
        fractal_sum = 0.0
        for i in range(self.dim):
            # Varying fractal dimension and roughness
            fractal_dim = 1.2 + 0.8 * np.sin(i * np.pi / max(1, self.dim - 1))
            roughness = 0.3 + 0.7 * np.cos(i * np.pi / max(1, self.dim - 1))
            phase = 0.4 * np.sin(i * np.pi / max(1, self.dim - 1))
            
            # Generate multi-fractal pattern
            noise_val = np.random.normal(0, 1) * (1 + roughness * x_norm[i]**4)
            fractal_sum += noise_val * np.cos(x_norm[i] * 8.0 + phase) * (1.0 / (1.0 + np.exp(-fractal_dim * x_norm[i])))
        
        # Adaptive harmonic component with dynamic frequency modulation
        harmonic_sum = 0.0
        for i in range(self.dim):
            # Dynamic scaling based on dimension index
            scale_factor = 2.0 + 3.0 * np.sin(i * np.pi / max(1, self.dim - 1))
            freq_mod = 4.0**(i % 5) if i % 5 != 0 else 1.0
            amp_mod = 1.5 + 1.0 * np.cos(i * np.pi / max(1, self.dim - 1))
            
            # Add phase coupling between dimensions
            phase_coupling = 0.0
            for j in range(min(3, i)):
                phase_coupling += np.sin(x_norm[i] * x_norm[j] * 2.0)
                
            harmonic_sum += amp_mod * np.sin(freq_mod * x_norm[i] * scale_factor + phase_coupling) * np.exp(-0.15 * i)
        
        # Enhanced cross-dimension coupling with polynomial interactions
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Polynomial interaction with varying degree
                poly_interaction = (x_norm[i]**3 + x_norm[j]**3) * np.cos(np.abs(x_norm[i] - x_norm[j]) * 2.0)
                cross_sum += poly_interaction * (1.0 / (1.0 + np.exp(-i * j)))
        
        # Novel penalty component for high-dimensional complexity
        penalty = 0.0
        if self.dim > 5:
            for i in range(self.dim):
                penalty += (x_norm[i]**2) * np.sin(10.0 * x_norm[i]) * np.cos(5.0 * x_norm[i])
        
        # Combine all components with new weighting scheme
        result = 0.25 * chaos_sum + 0.3 * fractal_sum + 0.2 * harmonic_sum + 0.25 * cross_sum + 0.1 * penalty
        
        # Enhanced conditioning factor with dimensionality and input distribution
        condition_factor = 1.0 + 0.4 * np.log(self.dim + 1) + 0.15 * np.std(x_norm) + 0.05 * np.mean(np.abs(x_norm))
        
        # Apply global transformation to increase non-convexity and add plateau control
        tanh_term = np.tanh(result)
        plateau_control = 1.0 + 0.3 * np.sum(np.abs(x_norm)**4) + 0.2 * np.sum(np.sin(x_norm)**2)
        result = tanh_term * plateau_control
        
        # Add final dimensionality-dependent scaling
        final_scaling = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return result * condition_factor * final_scaling