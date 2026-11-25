import numpy as np

class SinusoidalRidgeAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension
        self.ridge_frequencies = np.random.uniform(1.8, 7.0, dim)
        self.ridge_amplitudes = np.random.uniform(1.0, 4.0, dim)
        self.attractor_centers = np.random.uniform(-4.2, 4.2, dim)
        self.attractor_strengths = np.random.uniform(2.0, 5.0, dim)
        self.gradient_modulators = np.random.uniform(0.8, 3.0, dim)
        self.basin_probabilities = np.random.uniform(0.45, 0.98, dim)
        self.noise_levels = np.random.uniform(0.03, 0.2, dim)
        self.spectral_components = np.random.uniform(0.3, 1.5, dim)
        self.interaction_strengths = np.random.uniform(0.25, 0.7, dim)
        self.multimodal_amplitudes = np.random.uniform(1.2, 2.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add enhanced sinusoidal ridge components with improved modulation
        for i in range(self.dim):
            xi = x[i]
            freq = self.ridge_frequencies[i]
            amp = self.ridge_amplitudes[i]
            
            # Enhanced ridge structure with multiple harmonic components
            ridge_term = amp * np.sin(freq * xi) * np.cos(freq * xi) * np.tanh(xi)
            ridge_term += 0.6 * amp * np.sin(2 * freq * xi) * np.cos(2 * freq * xi)
            result += ridge_term
            
        # Add improved gradient modulation based on spectral components
        for i in range(self.dim):
            xi = x[i]
            modulator = self.gradient_modulators[i]
            spec_comp = self.spectral_components[i]
            
            # Enhanced spectral modulation with phase shifts
            gradient_mod = modulator * np.sin(spec_comp * xi + 0.5) * np.cos(spec_comp * xi - 0.3)
            result += 0.7 * gradient_mod * xi**2
            
        # Add improved probabilistic basin attraction with dynamic centers and strengths
        for i in range(self.dim):
            xi = x[i]
            center = self.attractor_centers[i]
            strength = self.attractor_strengths[i]
            prob = self.basin_probabilities[i]
            
            # Enhanced basin attraction with time-varying influence
            distance = np.abs(xi - center)
            basin_term = strength * np.exp(-0.4 * (distance / (1.0 + 0.08 * xi**2))) * (np.random.rand() < prob)
            result += basin_term
            
        # Add enhanced noise components with varying intensity and pattern
        for i in range(self.dim):
            xi = x[i]
            noise_level = self.noise_levels[i]
            
            # Enhanced stochastic noise component with dynamic scaling
            noise_component = noise_level * np.sin(15.0 * xi + 0.8 * i) * np.cos(7.0 * xi)
            result += noise_component
            
        # Add enhanced cross-dimensional interaction with sinusoidal coupling
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Enhanced sinusoidal coupling between dimensions with variable strength
                coupling_strength = 0.5 * np.sin(0.7 * (xi + xj)) * np.cos(0.5 * (xi - xj))
                cross_term = coupling_strength * np.exp(-0.2 * (xi**2 + xj**2))
                result += cross_term
                
        # Add enhanced global scaling with sinusoidal modulation
        global_scale = 1.0 + 0.5 * np.sin(np.sum(x) / self.dim)
        result *= global_scale
        
        # Add enhanced multimodal structure with multiple local minima and maxima
        multimodal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced multimodal components with higher-order harmonics
            multimodal_term += (xi**4 - 15*xi**2 + 25) * np.sin(3.0 * xi) * np.cos(2.0 * xi)
        result += 0.5 * multimodal_term
        
        # Add enhanced chaotic-like perturbation with improved complexity
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_perturbation += np.sin(30.0 * xi) * np.cos(20.0 * xi) * np.tanh(xi)
        result += 0.3 * chaotic_perturbation
        
        # Add additional harmonic structure for increased complexity
        harmonic_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            harmonic_term += 0.4 * np.sin(3.5 * xi) * np.cos(3.5 * xi) * (xi**2 - 1)
        result += harmonic_term
        
        # Add interaction term with higher-order coupling
        high_order_interaction = 0.0
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                high_order_interaction += 0.3 * (xi**3 + xj**3) * np.sin(0.6 * (xi + xj))
        result += high_order_interaction
        
        return result