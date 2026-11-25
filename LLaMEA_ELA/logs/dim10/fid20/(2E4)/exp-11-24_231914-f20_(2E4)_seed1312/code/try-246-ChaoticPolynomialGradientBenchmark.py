import numpy as np

class ChaoticPolynomialGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic tent map parameters
        self.tent_r = np.random.uniform(1.5, 3.0, size=dim)
        self.tent_x0 = np.random.uniform(0.1, 0.9, size=dim)
        # Polynomial interpolation parameters
        self.poly_degree = np.random.randint(2, 6, size=dim)
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, size=(dim, 6))
        # Gradient-based terrain modulation
        self.gradient_magnitude = np.random.uniform(0.5, 3.0, size=dim)
        self.gradient_direction = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        # Multi-scale harmonic components
        self.harmonic_freq = np.random.uniform(0.5, 5.0, size=dim)
        self.harmonic_amp = np.random.uniform(0.1, 2.0, size=dim)
        # Basin-like regions with chaotic dynamics
        self.basin_centers = np.random.uniform(-4.0, 4.0, size=5)
        self.basin_radii = np.random.uniform(0.5, 2.0, size=5)
        self.basin_depths = np.random.uniform(1.0, 5.0, size=5)
        # Dynamic scaling factors
        self.scale_factors = np.random.uniform(0.5, 2.0, size=dim)
        # Additional noise and perturbation parameters for improved fitness
        self.noise_level = np.random.uniform(0.01, 0.1, size=dim)
        self.perturbation_freq = np.random.uniform(0.1, 1.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component with enhanced dynamics
        tent_component = 0.0
        for i in range(self.dim):
            # Generate chaotic sequence with more iterations for stability
            tent_val = self.tent_x0[i]
            for _ in range(20):  # Increased iterations for better chaos
                if tent_val < 0.5:
                    tent_val = self.tent_r[i] * tent_val
                else:
                    tent_val = self.tent_r[i] * (1 - tent_val)
            tent_component += tent_val * np.sin(self.perturbation_freq[i] * x[i])
            
        # Polynomial interpolation component with improved weighting
        poly_component = 0.0
        for i in range(self.dim):
            x_scaled = x[i] / 5.0  # Normalize to [-1, 1]
            poly_val = 0.0
            for j in range(self.poly_degree[i]):
                poly_val += self.poly_coeffs[i, j] * (x_scaled ** (j + 1))  # Start from j=1
            poly_component += poly_val * np.cos(self.perturbation_freq[i] * x[i])
            
        # Gradient-based terrain modulation with improved structure
        grad_component = 0.0
        for i in range(self.dim):
            grad_val = 0.0
            for j in range(self.dim):
                grad_val += self.gradient_direction[i, j] * (x[j] - self.tent_x0[j])
            # Add a non-linear transformation to increase difficulty
            grad_component += self.gradient_magnitude[i] * np.tanh(grad_val)
            
        # Multi-scale harmonic component with enhanced complexity
        harmonic_component = 0.0
        for i in range(self.dim):
            # Combine multiple sine waves with different frequencies and amplitudes
            harmonic_val = 0.0
            for k in range(3):  # Three harmonic components
                freq = self.harmonic_freq[i] * (k + 1)
                amp = self.harmonic_amp[i] / (k + 1)
                harmonic_val += amp * np.sin(freq * x[i])
            harmonic_component += harmonic_val
            
        # Basin-like regions with chaotic dynamics and improved depth calculation
        basin_component = 0.0
        for i in range(5):
            min_dist = float('inf')
            dist_sum = 0.0
            for j in range(self.dim):
                dist = np.abs(x[j] - self.basin_centers[i])
                dist_sum += dist
                if dist < min_dist:
                    min_dist = dist
            # Use distance sum instead of minimum for better basin interaction
            if dist_sum <= self.basin_radii[i] * self.dim:
                basin_component += self.basin_depths[i] * (1 - dist_sum / (self.basin_radii[i] * self.dim))
                
        # Add noise to improve fitness score and robustness
        noise_component = 0.0
        for i in range(self.dim):
            noise_component += self.noise_level[i] * np.sin(x[i] * self.perturbation_freq[i])
            
        # Combined fitness function with optimized weights and structure
        return (1.2 * tent_component + 
                1.0 * poly_component + 
                0.8 * grad_component + 
                1.3 * harmonic_component + 
                0.9 * basin_component + 
                0.2 * noise_component)