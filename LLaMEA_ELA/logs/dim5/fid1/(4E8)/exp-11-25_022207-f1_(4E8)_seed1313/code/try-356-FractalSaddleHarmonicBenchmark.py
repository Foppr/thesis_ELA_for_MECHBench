import numpy as np

class FractalSaddleHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractal-like interaction parameters
        self.fractal_levels = np.random.uniform(1.0, 5.0, min(10, dim))
        self.saddle_strengths = np.logspace(0.5, 3.0, min(8, dim))
        self.harmonic_frequencies = np.logspace(0.5, 2.5, min(12, dim))
        # Multi-scale conditioning parameters
        self.conditioning_scales = np.logspace(1.0, 4.0, min(6, dim))
        # Create harmonic coupling matrix
        self.coupling_matrix = np.random.uniform(-1.0, 1.0, (min(8, dim), min(8, dim)))
        # Initialize noise and perturbation parameters
        self.noise_amplitudes = np.random.uniform(0.1, 1.0, min(6, dim))
        self.perturbation_scales = np.logspace(-1.0, 1.0, min(5, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Initialize result
        result = 0.0
        
        # Fractal-like cosine interactions with varying scales
        for i in range(self.dim):
            freq = self.harmonic_frequencies[i % len(self.harmonic_frequencies)]
            scale = self.conditioning_scales[i % len(self.conditioning_scales)]
            
            # Multi-scale harmonic term with fractal-like behavior
            fractal_term = np.cos(freq * x_norm[i]) * np.exp(-scale * np.abs(x_norm[i]))
            result += fractal_term
            
        # Saddle-point regions with dynamic strength
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_strength = self.saddle_strengths[i % len(self.saddle_strengths)]
            saddle_term += saddle_strength * (x_norm[i] ** 2) * np.cos(3.0 * x_norm[i])
            
        # Cross-dimensional harmonic coupling with fractal structure
        coupling_term = 0.0
        for i in range(min(len(self.coupling_matrix), self.dim)):
            for j in range(i + 1, min(len(self.coupling_matrix[0]), self.dim)):
                coupling_strength = self.coupling_matrix[i % len(self.coupling_matrix)][j % len(self.coupling_matrix[0])]
                coupling_term += coupling_strength * np.cos(x_norm[i] * x_norm[j])
                
        # Multi-scale conditioning with harmonic modulation
        conditioning_term = 0.0
        for i in range(self.dim):
            scale = self.conditioning_scales[i % len(self.conditioning_scales)]
            freq = self.harmonic_frequencies[i % len(self.harmonic_frequencies)]
            conditioning_term += np.sin(freq * x_norm[i]) * np.exp(-scale * x_norm[i]**2)
            
        # Add noise with fractal-like perturbations
        noise_term = 0.0
        for i in range(min(len(self.noise_amplitudes), self.dim)):
            noise_amp = self.noise_amplitudes[i]
            pert_scale = self.perturbation_scales[i % len(self.perturbation_scales)]
            noise_term += noise_amp * np.sin(pert_scale * x_norm[i]) * np.random.normal(0.0, 0.1)
            
        # Combine all components with adaptive weighting
        result = 0.5 * result + 0.3 * saddle_term + 0.2 * coupling_term + 0.4 * conditioning_term + 0.1 * noise_term
        
        return result