import numpy as np

class SinusoidalRidgeAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension
        self.ridge_frequencies = np.random.uniform(1.8, 7.0, dim)  # Increased range
        self.ridge_amplitudes = np.random.uniform(0.9, 4.0, dim)   # Increased range
        self.attractor_centers = np.random.uniform(-4.0, 4.0, dim)  # Slightly reduced range
        self.attractor_strengths = np.random.uniform(1.5, 5.0, dim)  # Increased range
        self.gradient_modulators = np.random.uniform(0.7, 3.0, dim)  # Increased range
        self.basin_probabilities = np.random.uniform(0.4, 0.98, dim)  # Increased range
        self.noise_levels = np.random.uniform(0.02, 0.15, dim)  # Increased range
        self.spectral_components = np.random.uniform(0.2, 1.5, dim)  # Increased range
        
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
            noise_component = noise_level * np.sin(12.0 * xi + 0.5 * i) * np.cos(6.0 * xi)
            result += noise_component
            
        # Add cross-dimensional interaction with sinusoidal coupling (enhanced coupling strength)
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Enhanced sinusoidal coupling between dimensions
                coupling_strength = 0.5 * np.sin(0.7 * (xi + xj)) * np.cos(0.5 * (xi - xj))  # Increased coupling strength
                cross_term = coupling_strength * np.exp(-0.1 * (xi**2 + xj**2))
                result += cross_term
                
        # Add global scaling with sinusoidal modulation
        global_scale = 1.0 + 0.4 * np.sin(np.sum(x) / self.dim)  # Increased modulation
        result *= global_scale
        
        # Add enhanced multimodal structure with multiple local minima
        multimodal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multiple sinusoidal components creating complex landscape
            multimodal_term += (xi**4 - 12*xi**2 + 8) * np.sin(2.5 * xi) * np.cos(1.8 * xi)  # Slightly altered frequencies
        result += 0.4 * multimodal_term  # Increased contribution
        
        # Add chaotic-like perturbation with improved complexity (enhanced chaotic component)
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_perturbation += np.sin(30.0 * xi) * np.cos(20.0 * xi) * np.tanh(xi)  # Increased frequencies and scaling
        result += 0.25 * chaotic_perturbation  # Increased contribution
        
        return result