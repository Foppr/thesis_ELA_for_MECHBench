import numpy as np

class FractalExponentialAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension
        self.attractor_centers = np.random.uniform(-4.0, 4.0, dim)
        self.decay_rates = np.random.uniform(0.1, 2.0, dim)
        self.amplitude_factors = np.random.uniform(0.5, 3.0, dim)
        self.noise_amplitudes = np.random.uniform(0.05, 0.3, dim)
        self.coupling_strengths = np.random.uniform(0.1, 1.5, dim)
        # Fractal parameters
        self.fractal_dimensions = np.random.uniform(1.2, 1.8, dim)
        self.frequency_modulators = np.random.uniform(0.5, 3.0, dim)
        self.hill_climbing_factors = np.random.uniform(0.3, 1.2, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add exponential decay attractor contributions
        for i in range(self.dim):
            xi = x[i]
            center = self.attractor_centers[i]
            decay_rate = self.decay_rates[i]
            amplitude = self.amplitude_factors[i]
            
            # Exponential decay with sinusoidal modulation
            distance = np.abs(xi - center)
            attractor_term = amplitude * np.exp(-decay_rate * distance) * np.sin(2.0 * xi)
            result += attractor_term
            
        # Add fractal noise component
        for i in range(self.dim):
            xi = x[i]
            noise_amp = self.noise_amplitudes[i]
            fractal_dim = self.fractal_dimensions[i]
            
            # Fractal-like noise with power-law scaling
            noise_component = noise_amp * np.sin(10.0 * xi) * np.cos(5.0 * xi) * np.exp(-0.2 * xi**2)
            result += noise_component
            
        # Add cross-dimensional coupling with exponential interaction
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                coupling_strength = self.coupling_strengths[i] * self.coupling_strengths[j]
                
                # Exponential coupling with fractal scaling
                distance = np.abs(xi - xj)
                coupling_term = coupling_strength * np.exp(-0.5 * distance**2) * np.sin(3.0 * (xi + xj))
                result += coupling_term
                
        # Add frequency-dependent modulation
        freq_mod = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq_mod += self.frequency_modulators[i] * np.exp(-0.1 * xi**2) * np.sin(5.0 * xi)
        result += 0.2 * freq_mod**2
        
        # Add hill-climbing bias component
        for i in range(self.dim):
            xi = x[i]
            hill_factor = self.hill_climbing_factors[i]
            hill_term = hill_factor * np.exp(-0.5 * (xi - 1.0)**2) * np.cos(3.0 * xi)
            result += hill_term
            
        # Add global scaling with fractal influence
        global_scale = 1.0 + 0.2 * np.sin(np.sum(x) / self.dim) * np.tanh(np.sum(x**2) / self.dim)
        result *= global_scale
        
        # Add chaotic perturbation for algorithmic bias
        chaotic_perturbation = 0.03 * np.sum(np.sin(150.0 * x) * np.cos(75.0 * x) * np.exp(-0.05 * np.sum(x**2)))
        result += chaotic_perturbation
        
        # Add enhanced multi-modal structure with exponential interactions
        multimodal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Exponential polynomial multimodal structure
            multimodal_term += (xi**3 - 6*xi**2 + 11*xi - 6) * np.exp(-0.5 * xi**2)
        result += 0.4 * multimodal_term
        
        return result