import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        np.random.seed(42)  # For reproducibility
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        # Additional random scaling for each dimension
        self.scales = np.random.uniform(0.5, 2.0, dim)
        # Adaptive noise parameters
        self.noise_scale = 1.2
        self.noise_frequency = 7.0
        # Fractal-like modulation parameters
        self.fractal_depth = 4
        self.fractal_amplitude = 3.0
        # Additional chaotic coupling parameters
        self.chaotic_coupling_strength = 2.0
        self.high_order_interaction_power = 5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and scaling
        x_transformed = self.rotation_matrix @ x * self.scales
        
        # Base quadratic term (ellipsoid)
        f_val = np.sum(x_transformed**2)
        
        # Add nested chaotic sine-wave perturbations with fractal structure
        for i in range(self.dim):
            # Base chaotic modulation with increased complexity
            chaotic_mod = np.sin(9.0 * x_transformed[i] + 3.0 * np.sin(7.0 * x_transformed[i]) + 0.5 * np.sin(11.0 * x_transformed[i]))
            # Nested fractal-like structure with higher depth
            nested_mod = 0.0
            for depth in range(self.fractal_depth):
                nested_mod += np.sin((depth + 1) * 4.0 * x_transformed[i]) * np.cos((depth + 1) * 3.0 * x_transformed[i]) * np.sin((depth + 1) * 2.0 * x_transformed[i])
            f_val += self.fractal_amplitude * (chaotic_mod + nested_mod)
            
        # Add complex interaction terms between dimensions with higher-order and chaotic coupling
        for i in range(self.dim - 5):
            # Higher-order interaction with fractal-like coupling
            interaction = self.chaotic_coupling_strength * x_transformed[i] ** self.high_order_interaction_power
            for j in range(1, 6):
                interaction *= x_transformed[i + j]
            fractal_coupling = np.sin(0.7 * x_transformed[i]) * np.cos(0.5 * x_transformed[i+1]) * np.sin(0.9 * x_transformed[i+2]) * np.cos(0.4 * x_transformed[i+3]) * np.sin(0.6 * x_transformed[i+4])
            f_val += interaction * fractal_coupling
            
        # Add a perturbed quintic term with chaotic modulation for increased complexity
        f_val += 0.15 * np.sum((x_transformed**5) * (1.0 + 0.5 * np.sin(9.0 * x_transformed) + 0.3 * np.cos(5.0 * x_transformed) + 0.2 * np.sin(13.0 * x_transformed)))
        
        # Add stochastic noise with adaptive variance and frequency
        noise = np.random.normal(0, self.noise_scale, self.dim)
        # Introduce frequency-dependent noise for increased ruggedness
        freq_noise = np.sin(self.noise_frequency * x_transformed) * noise
        f_val += np.sum(freq_noise * x_transformed)
        
        # Add a small constant to ensure positive fitness values
        f_val += 0.2
        
        return f_val