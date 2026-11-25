import numpy as np

class SinusoidalRidgeAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension with enhanced complexity
        self.ridge_frequencies = np.random.uniform(2.0, 8.0, dim)
        self.ridge_amplitudes = np.random.uniform(1.0, 4.0, dim)
        self.attractor_centers = np.random.uniform(-4.0, 4.0, dim)
        self.attractor_strengths = np.random.uniform(2.0, 5.0, dim)
        self.gradient_modulators = np.random.uniform(1.0, 3.0, dim)
        self.basin_probabilities = np.random.uniform(0.3, 0.98, dim)
        self.noise_levels = np.random.uniform(0.05, 0.2, dim)
        self.spectral_components = np.random.uniform(0.1, 1.5, dim)
        self.interaction_strengths = np.random.uniform(0.3, 0.8, dim)
        self.multimodal_amplitudes = np.random.uniform(1.2, 2.5, dim)
        self.chaotic_parameters = np.random.uniform(0.5, 2.0, dim)
        self.dynamic_coupling = np.random.uniform(0.1, 0.7, (dim, dim))
        self.frequency_modulators = np.random.uniform(0.8, 1.8, dim)
        self.phase_shifts = np.random.uniform(-0.5, 0.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Enhanced sinusoidal ridge components with dynamic frequency modulation
        for i in range(self.dim):
            xi = x[i]
            freq = self.ridge_frequencies[i] * (1.0 + 0.3 * np.sin(0.5 * xi))
            amp = self.ridge_amplitudes[i] * (1.0 + 0.2 * np.cos(0.3 * xi))
            
            # Multi-harmonic ridge structure with phase modulation
            ridge_term = amp * np.sin(freq * xi + self.phase_shifts[i]) * np.cos(freq * xi + self.phase_shifts[i])
            ridge_term += 0.6 * amp * np.sin(2 * freq * xi) * np.cos(2 * freq * xi)
            ridge_term += 0.3 * amp * np.sin(3 * freq * xi) * np.cos(3 * freq * xi)
            result += ridge_term
            
        # Improved gradient modulation with spectral and temporal components
        for i in range(self.dim):
            xi = x[i]
            modulator = self.gradient_modulators[i]
            spec_comp = self.spectral_components[i]
            
            # Multi-frequency gradient modulation with chaotic influence
            gradient_mod = modulator * np.sin(spec_comp * xi + 0.5) * np.cos(spec_comp * xi - 0.3)
            gradient_mod += 0.4 * np.sin(15.0 * xi) * np.cos(12.0 * xi) * np.tanh(xi)
            result += 0.7 * gradient_mod * xi**2
            
        # Enhanced probabilistic basin attraction with dynamic centers and time-varying strengths
        for i in range(self.dim):
            xi = x[i]
            center = self.attractor_centers[i] + 0.5 * np.sin(0.8 * xi)
            strength = self.attractor_strengths[i] * (1.0 + 0.2 * np.cos(0.4 * xi))
            prob = self.basin_probabilities[i] * (0.9 + 0.1 * np.sin(0.6 * xi))
            
            # Dynamic basin attraction with chaotic perturbations
            distance = np.abs(xi - center)
            basin_term = strength * np.exp(-0.25 * (distance / (1.0 + 0.03 * xi**2))) * (np.random.rand() < prob)
            result += basin_term
            
        # Enhanced noise components with fractal-like patterns and dynamic scaling
        for i in range(self.dim):
            xi = x[i]
            noise_level = self.noise_levels[i] * (1.0 + 0.3 * np.sin(20.0 * xi))
            
            # Fractal noise component with multi-scale influence
            noise_component = noise_level * np.sin(15.0 * xi + 0.7 * i) * np.cos(8.0 * xi)
            noise_component += 0.4 * np.sin(30.0 * xi) * np.cos(25.0 * xi)
            result += noise_component
            
        # Complex cross-dimensional interaction with dynamic coupling
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Dynamic sinusoidal coupling with time-varying strength
                coupling_strength = 0.5 * np.sin(0.7 * (xi + xj) + 0.2 * np.sin(0.3 * xi)) * np.cos(0.5 * (xi - xj) + 0.1 * np.cos(0.4 * xj))
                coupling_strength *= self.dynamic_coupling[i][j] * (1.0 + 0.2 * np.sin(0.6 * (xi + xj)))
                cross_term = coupling_strength * np.exp(-0.2 * (xi**2 + xj**2))
                result += cross_term
                
        # Enhanced global scaling with chaotic modulation
        global_scale = 1.0 + 0.5 * np.sin(np.sum(x) / self.dim + 0.3 * np.cos(0.4 * np.sum(x)))
        global_scale *= (1.0 + 0.2 * np.sin(10.0 * np.sum(x)**2))
        result *= global_scale
        
        # Advanced multimodal structure with higher-order chaotic components
        multimodal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic multimodal components with fractal-like behavior
            multimodal_term += (xi**4 - 15*xi**2 + 30) * np.sin(3.0 * xi) * np.cos(2.0 * xi)
            multimodal_term += 0.3 * np.sin(20.0 * xi) * np.cos(15.0 * xi) * np.tanh(xi)
        result += 0.5 * multimodal_term
        
        # Enhanced chaotic-like perturbation with fractal dimensionality
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_perturbation += np.sin(30.0 * xi) * np.cos(22.0 * xi) * np.tanh(xi)
            chaotic_perturbation += 0.5 * np.sin(40.0 * xi) * np.cos(35.0 * xi) * np.tanh(xi**2)
        result += 0.3 * chaotic_perturbation
        
        # Additional harmonic structures with fractal characteristics
        harmonic_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            harmonic_term += 0.4 * np.sin(4.0 * xi) * np.cos(4.0 * xi) * (xi**2 - 1)
            harmonic_term += 0.2 * np.sin(25.0 * xi) * np.cos(20.0 * xi) * np.tanh(xi)
        result += harmonic_term
        
        # Higher-order coupling with fractal-like interaction
        high_order_interaction = 0.0
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                # Fractal-like higher-order coupling
                interaction = 0.3 * (xi**3 + xj**3) * np.sin(0.6 * (xi + xj))
                interaction += 0.2 * xi**4 * xj * np.cos(0.5 * (xi - xj))
                high_order_interaction += interaction
        result += high_order_interaction
        
        # Add a novel hyper-chaotic component for increased complexity
        hyper_chaos = 0.0
        for i in range(self.dim):
            xi = x[i]
            hyper_chaos += np.sin(50.0 * xi) * np.cos(45.0 * xi) * np.tanh(xi) * (1.0 + 0.1 * np.sin(30.0 * xi))
        result += 0.25 * hyper_chaos
        
        return result