import numpy as np

class MultimodalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for chaotic attractors and fractal structures
        self.attractor_freq = [3.0 + 2.0 * np.sin(i * np.pi / (dim + 1)) for i in range(dim)]
        self.valley_fractal = [0.3 * np.cos(i * np.pi / (dim + 3)) for i in range(dim)]
        self.coupling_strength = 0.2 + 0.1 * np.sin(dim * np.pi / 8)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic multimodal component with fractal valley interactions
        multimodal = 0
        for i in range(self.dim):
            freq = self.attractor_freq[i]
            fractal = self.valley_fractal[i]
            # Chaotic attractor potential with fractal modulation
            attractor = np.sin(freq * x[i]) * np.cos(x[i] * 0.5) + 0.1 * np.sin(freq * x[i]**2)
            fractal_valley = fractal * np.sin(x[i] * 3) * (x[i]**4 - x[i]**2)
            multimodal += attractor + fractal_valley
            
        # Fractal valley structure with cross-dimensional coupling
        valley_structure = 0
        for i in range(self.dim):
            scale = (i + 1) / self.dim
            # Fractal quadratic valley with chaotic curvature
            valley = scale * (x[i]**2 - 2 * x[i] + 1)**1.5 + 0.15 * x[i]**5
            # Add fractal asymmetry through higher-order sine modulation
            fractal_term = 0.4 * np.sin(x[i] * 2) * scale**2
            valley_structure += valley + fractal_term
            
        # Chaotic noise-like perturbation with fractal frequency components
        noise_perturbation = 0
        for i in range(self.dim):
            freq1 = (i + 1) * np.pi / 3
            freq2 = (i + 1) * np.pi / 5
            freq3 = (i + 1) * np.pi / 7
            noise_perturbation += (
                np.sin(x[i] * freq1) + 
                0.15 * np.cos(x[i] * freq2) +
                0.08 * np.sin(x[i] * freq3) +
                0.05 * np.cos(x[i] * freq1 * 2)
            )
        
        # Enhanced interaction terms with fractal coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal interaction with dimensionally scaled coupling
                coupling = self.coupling_strength * (i + 1) * (j + 1)
                interaction += coupling * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Combine components with fractal weighting
        result = 2.5 * multimodal + 1.8 * valley_structure + 0.8 * noise_perturbation + 0.7 * interaction
        
        # Add fractal scaling factor based on dimensionality
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.05 * np.sin(self.dim * np.pi / 4)
        result *= scale_factor
        
        return result