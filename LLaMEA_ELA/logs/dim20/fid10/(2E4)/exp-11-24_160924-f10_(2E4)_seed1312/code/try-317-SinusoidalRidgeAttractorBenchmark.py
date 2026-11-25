import numpy as np

class SinusoidalRidgeAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension
        self.ridge_frequencies = np.random.uniform(2.0, 8.0, dim)
        self.ridge_amplitudes = np.random.uniform(1.0, 4.0, dim)
        self.attractor_centers = np.random.uniform(-4.0, 4.0, dim)
        self.attractor_strengths = np.random.uniform(2.0, 5.0, dim)
        self.gradient_modulators = np.random.uniform(0.5, 3.0, dim)
        self.basin_probabilities = np.random.uniform(0.3, 0.98, dim)
        self.noise_levels = np.random.uniform(0.01, 0.2, dim)
        self.spectral_components = np.random.uniform(0.1, 1.5, dim)
        self.interaction_strengths = np.random.uniform(0.1, 0.7, dim)
        self.multimodal_amplitudes = np.random.uniform(1.2, 2.5, dim)
        self.chaotic_parameters = np.random.uniform(0.8, 3.0, dim)
        self.frequency_modulators = np.random.uniform(0.6, 1.8, dim)
        self.phase_shifts = np.random.uniform(-0.5, 0.5, dim)
        self.hill_climbing_factors = np.random.uniform(0.1, 0.9, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add enhanced sinusoidal ridge components with improved modulation
        for i in range(self.dim):
            xi = x[i]
            freq = self.ridge_frequencies[i]
            amp = self.ridge_amplitudes[i]
            
            # Enhanced ridge structure with multiple harmonic components and phase shifts
            ridge_term = amp * np.sin(freq * xi + self.phase_shifts[i]) * np.cos(freq * xi + self.phase_shifts[i]) * np.tanh(xi)
            ridge_term += 0.5 * amp * np.sin(2 * freq * xi + self.phase_shifts[i]) * np.cos(2 * freq * xi + self.phase_shifts[i])
            ridge_term += 0.3 * amp * np.sin(3 * freq * xi + self.phase_shifts[i]) * np.cos(3 * freq * xi + self.phase_shifts[i])
            result += ridge_term
            
        # Add improved gradient modulation based on spectral components
        for i in range(self.dim):
            xi = x[i]
            modulator = self.gradient_modulators[i]
            spec_comp = self.spectral_components[i]
            
            # Enhanced spectral modulation with phase shifts and frequency modulation
            freq_mod = self.frequency_modulators[i]
            gradient_mod = modulator * np.sin(spec_comp * xi + 0.5 * freq_mod) * np.cos(spec_comp * xi - 0.3 * freq_mod)
            result += 0.6 * gradient_mod * xi**2
            
        # Add improved probabilistic basin attraction with dynamic centers and strengths
        for i in range(self.dim):
            xi = x[i]
            center = self.attractor_centers[i]
            strength = self.attractor_strengths[i]
            prob = self.basin_probabilities[i]
            
            # Enhanced basin attraction with time-varying influence and hill climbing factors
            distance = np.abs(xi - center)
            basin_term = strength * np.exp(-0.3 * (distance / (1.0 + 0.05 * xi**2))) * (np.random.rand() < prob)
            basin_term *= (1.0 + self.hill_climbing_factors[i] * np.sin(4.0 * xi))
            result += basin_term
            
        # Add enhanced noise components with varying intensity and pattern
        for i in range(self.dim):
            xi = x[i]
            noise_level = self.noise_levels[i]
            
            # Enhanced stochastic noise component with dynamic scaling and chaotic modulation
            noise_component = noise_level * np.sin(15.0 * xi + 0.7 * i) * np.cos(8.0 * xi)
            noise_component += 0.3 * np.sin(self.chaotic_parameters[i] * xi) * np.cos(self.chaotic_parameters[i] * xi)
            result += noise_component
            
        # Add enhanced cross-dimensional interaction with sinusoidal coupling
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Enhanced sinusoidal coupling between dimensions with variable strength and chaotic modulation
                coupling_strength = 0.4 * np.sin(0.6 * (xi + xj)) * np.cos(0.4 * (xi - xj))
                coupling_strength += 0.1 * np.sin(self.chaotic_parameters[i] * xi) * np.cos(self.chaotic_parameters[j] * xj)
                cross_term = coupling_strength * np.exp(-0.15 * (xi**2 + xj**2))
                result += cross_term
                
        # Add enhanced global scaling with sinusoidal modulation
        global_scale = 1.0 + 0.4 * np.sin(np.sum(x) / self.dim)
        global_scale *= (1.0 + 0.2 * np.cos(0.5 * np.sum(x)))
        result *= global_scale
        
        # Add enhanced multimodal structure with multiple local minima and maxima
        multimodal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced multimodal components with higher-order harmonics and chaotic perturbations
            multimodal_term += (xi**4 - 12*xi**2 + 20) * np.sin(2.5 * xi) * np.cos(1.8 * xi)
            multimodal_term += 0.3 * np.sin(self.chaotic_parameters[i] * xi**2) * np.cos(self.chaotic_parameters[i] * xi)
        result += 0.4 * multimodal_term
        
        # Add enhanced chaotic-like perturbation with improved complexity and phase modulation
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_perturbation += np.sin(25.0 * xi + self.phase_shifts[i]) * np.cos(18.0 * xi + self.phase_shifts[i]) * np.tanh(xi)
            chaotic_perturbation += 0.2 * np.sin(30.0 * xi + self.phase_shifts[i]) * np.cos(22.0 * xi + self.phase_shifts[i])
        result += 0.2 * chaotic_perturbation
        
        # Add additional harmonic structure for increased complexity with phase modulation
        harmonic_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            harmonic_term += 0.3 * np.sin(3.0 * xi + self.phase_shifts[i]) * np.cos(3.0 * xi + self.phase_shifts[i]) * (xi**2 - 1)
            harmonic_term += 0.1 * np.sin(5.0 * xi + self.phase_shifts[i]) * np.cos(5.0 * xi + self.phase_shifts[i])
        result += harmonic_term
        
        # Add interaction term with higher-order coupling and chaotic modulation
        high_order_interaction = 0.0
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                high_order_interaction += 0.2 * (xi**3 + xj**3) * np.sin(0.5 * (xi + xj))
                high_order_interaction += 0.1 * np.sin(self.chaotic_parameters[i] * xi) * np.cos(self.chaotic_parameters[j] * xj)
        result += high_order_interaction
        
        # Add enhanced ridge structure with fractal-like properties
        fractal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            fractal_term += 0.15 * np.sin(10.0 * xi) * np.cos(7.0 * xi) * (np.abs(xi) < 2.0)
        result += fractal_term
        
        return result