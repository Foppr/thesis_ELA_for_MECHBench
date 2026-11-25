import numpy as np

class NestedFractalSaddleHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize nested fractal parameters with hierarchical structure
        self.fractal_depths = np.random.uniform(2.0, 8.0, min(12, dim))
        self.saddle_strengths = np.logspace(0.3, 3.5, min(10, dim))
        self.harmonic_frequencies = np.logspace(0.2, 3.0, min(15, dim))
        # Multi-scale hierarchical conditioning
        self.conditioning_scales = np.logspace(0.5, 4.5, min(8, dim))
        # Create nested coupling matrices for hierarchical structure
        self.coupling_matrices = []
        for i in range(min(5, dim // 2 + 1)):
            matrix_size = min(6, dim // (i + 1) + 1)
            self.coupling_matrices.append(np.random.uniform(-0.5, 0.5, (matrix_size, matrix_size)))
        # Initialize noise and perturbation parameters with chaotic variations
        self.noise_amplitudes = np.random.uniform(0.05, 1.5, min(8, dim))
        self.perturbation_scales = np.logspace(-1.5, 1.5, min(7, dim))
        # Add chaotic modulation parameters
        self.modulation_factors = np.random.uniform(0.5, 2.0, min(6, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Initialize result
        result = 0.0
        
        # Nested fractal-like cosine interactions with hierarchical scales
        for i in range(self.dim):
            depth = self.fractal_depths[i % len(self.fractal_depths)]
            freq = self.harmonic_frequencies[i % len(self.harmonic_frequencies)]
            scale = self.conditioning_scales[i % len(self.conditioning_scales)]
            
            # Nested fractal term with chaotic modulation
            nested_term = np.cos(freq * x_norm[i]) * np.exp(-scale * np.abs(x_norm[i])) * np.sin(depth * x_norm[i])
            result += nested_term
            
        # Adaptive saddle-point regions with dynamic strength and chaotic modulation
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_strength = self.saddle_strengths[i % len(self.saddle_strengths)]
            modulation = self.modulation_factors[i % len(self.modulation_factors)]
            saddle_term += saddle_strength * (x_norm[i] ** 2) * np.cos(3.0 * x_norm[i]) * modulation
            
        # Hierarchical cross-dimensional harmonic coupling with nested structure
        coupling_term = 0.0
        for level, matrix in enumerate(self.coupling_matrices):
            if level >= self.dim // 2:
                break
            start_idx = level * (self.dim // (level + 1) + 1)
            end_idx = min(start_idx + len(matrix), self.dim)
            for i in range(len(matrix)):
                for j in range(i + 1, len(matrix[0])):
                    if start_idx + i < self.dim and start_idx + j < self.dim:
                        coupling_strength = matrix[i % len(matrix)][j % len(matrix[0])]
                        coupling_term += coupling_strength * np.cos(x_norm[start_idx + i] * x_norm[start_idx + j])
                
        # Hierarchical conditioning with nested harmonic modulation
        conditioning_term = 0.0
        for i in range(self.dim):
            scale = self.conditioning_scales[i % len(self.conditioning_scales)]
            freq = self.harmonic_frequencies[i % len(self.harmonic_frequencies)]
            modulation = self.modulation_factors[i % len(self.modulation_factors)]
            conditioning_term += np.sin(freq * x_norm[i]) * np.exp(-scale * x_norm[i]**2) * modulation
            
        # Add chaotic noise with nested perturbations
        noise_term = 0.0
        for i in range(min(len(self.noise_amplitudes), self.dim)):
            noise_amp = self.noise_amplitudes[i]
            pert_scale = self.perturbation_scales[i % len(self.perturbation_scales)]
            # Nested chaotic perturbation structure
            nested_pert = np.sin(pert_scale * x_norm[i]) * np.cos(pert_scale * x_norm[i] ** 2)
            noise_term += noise_amp * nested_pert * np.random.normal(0.0, 0.1)
            
        # Combine all components with hierarchical weighting
        result = 0.3 * result + 0.4 * saddle_term + 0.2 * coupling_term + 0.5 * conditioning_term + 0.1 * noise_term
        
        return result