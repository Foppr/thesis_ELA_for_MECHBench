import numpy as np

class SinusoidalRidgeAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension with enhanced variability
        self.ridge_frequencies = np.random.uniform(2.0, 8.0, dim)  # Increased range
        self.ridge_amplitudes = np.random.uniform(1.0, 5.0, dim)   # Increased range
        self.attractor_centers = np.random.uniform(-4.8, 4.8, dim)  # Extended range
        self.attractor_strengths = np.random.uniform(1.5, 6.0, dim)  # Increased range
        self.gradient_modulators = np.random.uniform(0.8, 3.0, dim)  # Increased range
        self.basin_probabilities = np.random.uniform(0.4, 0.98, dim)  # Increased range
        self.noise_levels = np.random.uniform(0.02, 0.15, dim)  # Increased range
        self.spectral_components = np.random.uniform(0.2, 1.5, dim)  # Increased range
        self.coupling_strengths = np.random.uniform(0.6, 1.2, dim)  # Enhanced coupling
        self.multimodal_frequencies = np.random.uniform(1.8, 3.5, dim)  # Increased complexity
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add sinusoidal ridge components with dynamic modulation
        for i in range(self.dim):
            xi = x[i]
            freq = self.ridge_frequencies[i]
            amp = self.ridge_amplitudes[i]
            
            # Enhanced sinusoidal ridge structure with varying frequency and amplitude
            ridge_term = amp * np.sin(freq * xi) * np.cos(freq * xi) * np.tanh(xi)
            result += ridge_term
            
        # Add gradient modulation based on spectral components
        for i in range(self.dim):
            xi = x[i]
            modulator = self.gradient_modulators[i]
            spec_comp = self.spectral_components[i]
            
            # Spectral modulation of gradient direction with enhanced complexity
            gradient_mod = modulator * np.sin(spec_comp * xi) * np.cos(spec_comp * xi) * np.tanh(xi)
            result += 0.6 * gradient_mod * xi**2
            
        # Add probabilistic basin attraction with dynamic centers
        for i in range(self.dim):
            xi = x[i]
            center = self.attractor_centers[i]
            strength = self.attractor_strengths[i]
            prob = self.basin_probabilities[i]
            
            # Basin attraction with probabilistic influence and enhanced dynamics
            distance = np.abs(xi - center)
            basin_term = strength * np.exp(-0.5 * (distance / (1.0 + 0.2 * xi**2))) * (np.random.rand() < prob)
            result += basin_term
            
        # Add noise components with varying intensity and pattern
        for i in range(self.dim):
            xi = x[i]
            noise_level = self.noise_levels[i]
            
            # Stochastic noise component with dynamic scaling and enhanced complexity
            noise_component = noise_level * np.sin(15.0 * xi + 0.7 * i) * np.cos(8.0 * xi) * np.tanh(xi)
            result += noise_component
            
        # Add cross-dimensional interaction with sinusoidal coupling (significantly enhanced coupling strength)
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Enhanced sinusoidal coupling between dimensions with increased complexity
                coupling_strength = 0.6 * np.sin(0.8 * (xi + xj)) * np.cos(0.5 * (xi - xj)) * np.tanh(xi) * np.tanh(xj)
                cross_term = coupling_strength * np.exp(-0.15 * (xi**2 + xj**2))
                result += cross_term
                
        # Add global scaling with sinusoidal modulation
        global_scale = 1.0 + 0.5 * np.sin(np.sum(x) / self.dim) * np.cos(np.sum(x) / (self.dim * 2))  # Increased modulation complexity
        result *= global_scale
        
        # Add enhanced multimodal structure with multiple local minima
        multimodal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = self.multimodal_frequencies[i]
            # Multiple sinusoidal components creating complex landscape with higher frequency modulation
            multimodal_term += (xi**4 - 12*xi**2 + 8) * np.sin(freq * xi) * np.cos(freq * xi)
        result += 0.5 * multimodal_term  # Increased contribution
        
        # Add chaotic-like perturbation with improved complexity
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_perturbation += np.sin(30.0 * xi) * np.cos(22.0 * xi) * np.tanh(xi) * np.exp(-0.1 * xi**2)
        result += 0.3 * chaotic_perturbation  # Increased contribution
        
        return result