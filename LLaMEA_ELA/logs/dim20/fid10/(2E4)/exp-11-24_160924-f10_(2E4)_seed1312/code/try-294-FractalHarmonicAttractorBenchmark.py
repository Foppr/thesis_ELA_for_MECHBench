import numpy as np

class FractalHarmonicAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize fractal parameters for each dimension
        self.fractal_exponents = np.random.uniform(0.3, 1.8, dim)
        self.harmonic_amplitudes = np.random.uniform(1.0, 3.0, dim)
        self.harmonic_frequencies = np.random.uniform(0.5, 4.0, dim)
        self.log_scaling_factors = np.random.uniform(0.5, 2.0, dim)
        self.multi_scale_weights = np.random.uniform(0.1, 1.0, dim)
        self.interaction_strengths = np.random.uniform(0.5, 2.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add fractal gradient contributions with log scaling
        for i in range(self.dim):
            xi = x[i]
            exp = self.fractal_exponents[i]
            amp = self.harmonic_amplitudes[i]
            freq = self.harmonic_frequencies[i]
            log_scale = self.log_scaling_factors[i]
            
            # Fractal-like structure with logarithmic scaling
            fractal_term = amp * np.log(1.0 + log_scale * np.abs(xi))**exp
            result += fractal_term
            
        # Add multi-scale harmonic interactions
        for i in range(self.dim):
            xi = x[i]
            amp = self.harmonic_amplitudes[i]
            freq = self.harmonic_frequencies[i]
            weight = self.multi_scale_weights[i]
            
            # Multi-scale harmonic components with varying frequencies and weights
            harmonic_term = weight * amp * np.sin(freq * xi) * np.cos(0.5 * freq * xi)
            result += harmonic_term
            
        # Add cross-dimensional multi-scale interactions
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                strength = self.interaction_strengths[i] * self.interaction_strengths[j]
                
                # Multi-scale interaction with logarithmic coupling
                log_coupling = np.log(1.0 + 0.5 * (xi**2 + xj**2))
                interaction_term = strength * log_coupling * np.sin(xi + xj) * np.cos(xi - xj)
                result += interaction_term
                
        # Add global fractal scaling based on input magnitude
        input_magnitude = np.sqrt(np.sum(x**2))
        global_fractal_scale = 1.0 + 0.5 * np.log(1.0 + input_magnitude)
        result *= global_fractal_scale
        
        # Add asymmetric multimodal structure with self-similar patterns
        multimodal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Self-similar multimodal structure with varying scales
            scale_factor = 1.0 + 0.3 * np.sin(xi)
            multimodal_term += (xi**3 - 3*xi) * scale_factor * np.cos(2.0 * xi)
        result += 0.3 * multimodal_term
        
        # Add noise-like fractal components
        noise_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractal noise with varying intensity
            noise_intensity = 0.1 + 0.2 * np.sin(xi) * np.cos(0.5 * xi)
            noise_component = noise_intensity * np.sin(10.0 * xi + i) * np.tanh(xi)
            noise_term += noise_component
        result += noise_term
        
        return result