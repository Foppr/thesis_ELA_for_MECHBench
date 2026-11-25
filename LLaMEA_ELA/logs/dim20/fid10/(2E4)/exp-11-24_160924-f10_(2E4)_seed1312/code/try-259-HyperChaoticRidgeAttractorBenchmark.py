import numpy as np

class HyperChaoticRidgeAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize hyperchaotic parameters for each dimension
        self.attractor_centers = np.random.uniform(-4.0, 4.0, dim)
        self.attractor_strengths = np.random.uniform(2.0, 6.0, dim)
        self.ridge_parameters = np.random.uniform(1.0, 3.0, dim)
        self.noise_levels = np.random.uniform(0.02, 0.15, dim)
        self.frequency_modulators = np.random.uniform(1.0, 3.0, dim)
        # Hyperchaotic and fractal parameters
        self.fractal_dimensions = np.random.uniform(1.2, 1.8, dim)
        self.saddle_strengths = np.random.uniform(1.0, 4.0, dim)
        self.coupling_exponents = np.random.uniform(0.3, 1.7, dim)
        # Hyperchaotic coupling coefficients
        self.hyperchaos_coefficients = np.random.uniform(0.5, 2.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add hyperchaotic attractor contributions with fractal modulation
        for i in range(self.dim):
            xi = x[i]
            center = self.attractor_centers[i]
            strength = self.attractor_strengths[i]
            ridge_param = self.ridge_parameters[i]
            fractal_dim = self.fractal_dimensions[i]
            
            # Hyperchaotic fractal attractor with multi-scale modulation
            distance = np.abs(xi - center)
            fractal_term = strength * np.exp(-0.5 * (distance / (1.0 + 0.2 * xi**3))**fractal_dim)
            
            # Ridge-like gradient flow with hyperbolic scaling
            ridge_component = ridge_param * np.sin(5.0 * xi) * np.cos(3.0 * xi) * np.tanh(xi**2)
            
            result += fractal_term + ridge_component
            
        # Add hyperchaotic saddle point contributions
        for i in range(self.dim):
            xi = x[i]
            saddle_strength = self.saddle_strengths[i]
            # Hyperchaotic saddle point with multi-exponential decay
            saddle_term = saddle_strength * np.exp(-0.5 * xi**3) * np.sin(15.0 * xi) * np.cos(7.0 * xi)
            result += saddle_term
            
        # Add cross-dimensional hyperchaotic coupling with fractal scaling
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Hyperchaotic coupling strength with multi-frequency modulation
                coupling_strength = 0.7 * (1.0 + np.sin(0.5 * (i - j))) * (1.0 + 0.3 * np.sin(xi + xj)) * (1.0 + 0.2 * np.cos(xi * xj))
                
                # Fractal coupling with multi-scale interaction
                exponent = self.coupling_exponents[i] * self.coupling_exponents[j] * (1.0 + 0.1 * np.sin(i + j))
                cross_term = coupling_strength * np.power(np.abs(xi - xj), exponent) * np.cos(0.7 * (xi + xj)) * np.sin(0.3 * xi * xj)
                result += cross_term
                
        # Add dimensionally adaptive noise with hyperbolic fractal characteristics
        for i in range(self.dim):
            xi = x[i]
            noise_level = self.noise_levels[i] * (1.0 + 0.3 * np.sin(0.8 * i)) * (1.0 + 0.15 * np.cos(xi**2))
            noise_component = noise_level * np.sin(15.0 * xi + 0.7 * i) * np.cos(8.0 * xi) * np.tanh(xi)
            result += noise_component
            
        # Add hyperfrequency-dependent modulation for enhanced complexity
        freq_mod = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq_mod += self.frequency_modulators[i] * np.sin(6.0 * xi + 0.5 * i) * np.tanh(xi**2)
        result += 0.15 * freq_mod**3
        
        # Add global scaling with hyperbolic transformation and fractal influence
        global_scale = 1.0 + 0.4 * np.tanh(np.sum(x**2) / self.dim) * np.prod(np.cos(x / 4.0))
        result *= global_scale
        
        # Add hyperchaotic perturbation to increase algorithmic bias
        chaotic_perturbation = 0.1 * np.sum(np.sin(200.0 * x) * np.cos(100.0 * x) * np.exp(-0.15 * np.sum(x**3)))
        result += chaotic_perturbation
        
        # Add enhanced hyper-multi-modal structure with better fitness discrimination
        multimodal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Add multiple local minima with varying depths and hyperbolic modulation
            multimodal_term += (xi**5 - 20*xi**3 + 10*xi**2) * np.cos(0.7 * xi) * np.tanh(xi)
        result += 0.4 * multimodal_term
        
        # Add adaptive ridge modulation with hyperbolic coupling
        adaptive_ridge = 0.0
        for i in range(self.dim):
            xi = x[i]
            adaptive_ridge += self.hyperchaos_coefficients[i] * np.sin(2.0 * xi) * np.cos(4.0 * xi) * np.tanh(xi**3)
        result += 0.2 * adaptive_ridge
        
        return result