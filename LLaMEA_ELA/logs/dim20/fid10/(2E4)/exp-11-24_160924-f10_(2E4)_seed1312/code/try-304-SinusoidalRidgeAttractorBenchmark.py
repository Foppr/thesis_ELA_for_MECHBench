import numpy as np

class SinusoidalRidgeAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension
        self.ridge_frequencies = np.random.uniform(1.0, 6.0, dim)
        self.ridge_amplitudes = np.random.uniform(0.5, 4.0, dim)
        self.attractor_centers = np.random.uniform(-3.5, 3.5, dim)
        self.attractor_strengths = np.random.uniform(1.5, 5.0, dim)
        self.gradient_modulators = np.random.uniform(0.3, 2.5, dim)
        self.basin_probabilities = np.random.uniform(0.2, 0.85, dim)
        self.noise_levels = np.random.uniform(0.02, 0.15, dim)
        self.spectral_components = np.random.uniform(0.05, 1.2, dim)
        self.cross_coupling_strengths = np.random.uniform(0.2, 0.8, (dim, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add enhanced sinusoidal ridge components with dynamic modulation
        for i in range(self.dim):
            xi = x[i]
            freq = self.ridge_frequencies[i]
            amp = self.ridge_amplitudes[i]
            
            # Enhanced ridge structure with multiple harmonic components
            ridge_term = amp * np.sin(freq * xi) * np.cos(freq * xi) * np.tanh(xi)
            ridge_term += 0.5 * amp * np.sin(2 * freq * xi) * np.cos(2 * freq * xi)
            result += ridge_term
            
        # Add adaptive gradient modulation based on spectral components
        for i in range(self.dim):
            xi = x[i]
            modulator = self.gradient_modulators[i]
            spec_comp = self.spectral_components[i]
            
            # Adaptive spectral modulation with dynamic scaling
            gradient_mod = modulator * np.sin(spec_comp * xi) * np.cos(spec_comp * xi)
            gradient_mod += 0.3 * np.sin(3 * spec_comp * xi) * np.cos(3 * spec_comp * xi)
            result += 0.4 * gradient_mod * xi**2
            
        # Add probabilistic basin attraction with enhanced dynamic centers
        for i in range(self.dim):
            xi = x[i]
            center = self.attractor_centers[i]
            strength = self.attractor_strengths[i]
            prob = self.basin_probabilities[i]
            
            # Enhanced basin attraction with non-linear distance scaling
            distance = np.abs(xi - center)
            basin_term = strength * np.exp(-0.3 * (distance**2) / (1.0 + 0.2 * xi**2)) * (np.random.rand() < prob)
            result += basin_term
            
        # Add enhanced noise components with improved stochastic patterns
        for i in range(self.dim):
            xi = x[i]
            noise_level = self.noise_levels[i]
            
            # Improved stochastic noise component with multi-frequency pattern
            noise_component = noise_level * (np.sin(15.0 * xi + 0.3 * i) * np.cos(7.0 * xi) + 
                                           0.5 * np.sin(8.0 * xi + 0.7 * i) * np.cos(4.0 * xi))
            result += noise_component
            
        # Add enhanced cross-dimensional interaction with adaptive coupling
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Adaptive sinusoidal coupling between dimensions
                coupling_strength = self.cross_coupling_strengths[i][j] * np.sin(0.3 * (xi + xj)) * np.cos(0.4 * (xi - xj))
                cross_term = coupling_strength * np.exp(-0.15 * (xi**2 + xj**2))
                result += cross_term
                
        # Add global scaling with enhanced sinusoidal modulation
        global_scale = 1.0 + 0.4 * np.sin(np.sum(x) / self.dim)
        global_scale += 0.2 * np.cos(2 * np.sum(x) / self.dim)
        result *= global_scale
        
        # Add improved multimodal structure with multiple local minima
        multimodal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced multimodal components with complex interaction
            multimodal_term += (xi**4 - 12*xi**2 + 20) * np.sin(3.0 * xi) * np.cos(2.0 * xi)
            multimodal_term += 0.5 * (xi**6 - 15*xi**4 + 75*xi**2 - 125) * np.sin(xi)
        result += 0.4 * multimodal_term
        
        # Add improved chaotic-like perturbation with better complexity
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_perturbation += np.sin(25.0 * xi) * np.cos(18.0 * xi) * np.tanh(xi)
            chaotic_perturbation += 0.3 * np.sin(40.0 * xi) * np.cos(30.0 * xi)
        result += 0.2 * chaotic_perturbation
        
        return result