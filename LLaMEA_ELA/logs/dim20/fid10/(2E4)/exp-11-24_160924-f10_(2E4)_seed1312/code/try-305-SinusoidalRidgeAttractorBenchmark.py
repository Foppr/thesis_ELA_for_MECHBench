import numpy as np

class SinusoidalRidgeAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension
        self.ridge_frequencies = np.random.uniform(1.5, 6.0, dim)  # Slightly increased range
        self.ridge_amplitudes = np.random.uniform(0.7, 3.5, dim)   # Slightly increased range
        self.attractor_centers = np.random.uniform(-3.5, 3.5, dim) # Slightly reduced range
        self.attractor_strengths = np.random.uniform(1.2, 4.5, dim) # Slightly increased range
        self.gradient_modulators = np.random.uniform(0.6, 2.5, dim) # Slightly increased range
        self.basin_probabilities = np.random.uniform(0.2, 0.8, dim) # Reduced range for more challenge
        self.noise_levels = np.random.uniform(0.02, 0.12, dim) # Slightly increased range
        self.spectral_components = np.random.uniform(0.15, 1.2, dim) # Slightly increased range
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add sinusoidal ridge components with dynamic modulation
        for i in range(self.dim):
            xi = x[i]
            freq = self.ridge_frequencies[i]
            amp = self.ridge_amplitudes[i]
            
            # Sinusoidal ridge structure with varying frequency and amplitude
            ridge_term = amp * np.sin(freq * xi) * np.cos(freq * xi) * np.tanh(xi)
            result += ridge_term
            
        # Add gradient modulation based on spectral components
        for i in range(self.dim):
            xi = x[i]
            modulator = self.gradient_modulators[i]
            spec_comp = self.spectral_components[i]
            
            # Spectral modulation of gradient direction
            gradient_mod = modulator * np.sin(spec_comp * xi) * np.cos(spec_comp * xi)
            result += 0.5 * gradient_mod * xi**2
            
        # Add probabilistic basin attraction with dynamic centers
        for i in range(self.dim):
            xi = x[i]
            center = self.attractor_centers[i]
            strength = self.attractor_strengths[i]
            prob = self.basin_probabilities[i]
            
            # Basin attraction with probabilistic influence
            distance = np.abs(xi - center)
            basin_term = strength * np.exp(-0.5 * (distance / (1.0 + 0.1 * xi**2))) * (np.random.rand() < prob)
            result += basin_term
            
        # Add noise components with varying intensity and pattern
        for i in range(self.dim):
            xi = x[i]
            noise_level = self.noise_levels[i]
            
            # Stochastic noise component with dynamic scaling
            noise_component = noise_level * np.sin(10.0 * xi + 0.5 * i) * np.cos(5.0 * xi)
            result += noise_component
            
        # Add cross-dimensional interaction with sinusoidal coupling
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Sinusoidal coupling between dimensions
                coupling_strength = 0.3 * np.sin(0.5 * (xi + xj)) * np.cos(0.3 * (xi - xj))
                cross_term = coupling_strength * np.exp(-0.1 * (xi**2 + xj**2))
                result += cross_term
                
        # Add global scaling with sinusoidal modulation
        global_scale = 1.0 + 0.3 * np.sin(np.sum(x) / self.dim)
        result *= global_scale
        
        # Add enhanced multimodal structure with multiple local minima
        multimodal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multiple sinusoidal components creating complex landscape
            multimodal_term += (xi**4 - 10*xi**2 + 5) * np.sin(2.0 * xi) * np.cos(1.5 * xi)
        result += 0.3 * multimodal_term
        
        # Add chaotic-like perturbation with improved complexity
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_perturbation += np.sin(25.0 * xi) * np.cos(20.0 * xi) * np.tanh(xi) # Increased frequencies
        result += 0.18 * chaotic_perturbation # Slightly increased perturbation
        
        return result