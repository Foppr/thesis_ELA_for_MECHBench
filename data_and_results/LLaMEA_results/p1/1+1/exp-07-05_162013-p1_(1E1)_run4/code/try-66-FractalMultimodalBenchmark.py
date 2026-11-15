import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.peaks = []
        self.amplitude_modulation = []
        self._generate_fractal_structure()
        
    def _generate_fractal_structure(self):
        # Generate fractal peak locations using recursive golden ratio subdivision
        self.peaks = []
        for i in range(2**self.dim):
            peak = []
            for j in range(self.dim):
                # Use binary representation to create fractal structure
                bit = (i >> j) & 1
                peak.append(-5.0 + bit * 10.0)
            self.peaks.append(np.array(peak))
            
        # Generate amplitude modulation sequence using chaotic sine wave
        self.amplitude_modulation = []
        for i in range(self.dim):
            self.amplitude_modulation.append(0.5 + 0.5 * np.sin(i * np.pi / self.dim + 1.0))
            
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Fractal Gaussian peaks with recursive structure
        for i, peak in enumerate(self.peaks):
            # Calculate distance to peak
            dist = np.sum((x - peak)**2)
            # Apply fractal scaling with chaotic amplitude modulation
            scale = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
            amp = 1.0 + 0.3 * np.sin(i * 0.785) * self.amplitude_modulation[i % len(self.amplitude_modulation)]
            result += amp * np.exp(-dist / (2.0 * scale**2))
            
        # Add cross-dimensional coupling with fractal interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal coupling strength based on position
                coupling = 0.1 * (1 + np.sin(x[i] * x[j] * 0.1))
                result += coupling * np.sin(x[i] + x[j])
                
        # Add self-similar harmonic components
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5)
            result += 0.05 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            
        # Add fractal noise with chaotic frequency modulation
        noise_freq = 1.0 + 2.0 * np.sin(np.sum(x) * 0.1)
        result += 0.02 * np.sin(noise_freq * np.sum(x))
        
        # Add global scaling with fractal dimension effect
        fractal_dim = 1.5 + 0.5 * np.sin(self.dim * 0.3)
        result += 0.01 * np.sum(x**(2 * fractal_dim))
        
        return result