import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component with chaotic sine-cosine patterns and quantum interference
        fractal = 0.0
        for i in range(self.dim):
            # Chaotic pattern with quantum-like phase interference
            freq = 3.0 + 1.5 * np.sin(x_scaled[i] * 4.0) * np.cos(x_scaled[i] * 2.0)
            amp = 1.2 + 0.4 * np.sin(x_scaled[i] * 3.0) * np.cos(x_scaled[i] * 1.5)
            phase = np.sin(x_scaled[i] * 7.0) * np.cos(x_scaled[i] * 5.0)
            fractal += amp * np.sin(freq * x_scaled[i] + phase) * np.cos(freq * x_scaled[i] * 0.3 + phase)
        
        # Quantum attractor fields with superposition states
        attractor = 0.0
        for i in range(self.dim):
            # Multiple quantum attractor centers with complex amplitudes
            center1 = np.sin(i * 0.8) * 0.9 + 0.1 * np.cos(i * 0.3)
            center2 = np.cos(i * 0.6) * 0.7 + 0.2 * np.sin(i * 0.4)
            strength1 = 1.5 + 0.3 * np.sin(i * 0.9)
            strength2 = 1.2 + 0.2 * np.cos(i * 0.5)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            
            # Quantum superposition of attractor fields
            attractor += strength1 * np.exp(-dist1) * np.sin(x_scaled[i] * 3.0) + \
                        strength2 * np.exp(-dist2) * np.cos(x_scaled[i] * 2.0)
        
        # Exponentially increasing complexity with chaotic interaction terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction range
                # Chaotic interaction weights with exponential scaling
                weight = np.exp(2.0 * (1.0 + np.abs(i - j))) / (1.0 + np.abs(i - j))
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.exp(-np.abs(x_scaled[i] - x_scaled[j]))
        
        # Multi-scale fractal component with quantum self-similarity and chaos
        multiscale = 0.0
        for scale in [1, 2, 3, 6]:  # Increased scale values and added 6
            for i in range(self.dim):
                # Quantum-like multi-scale pattern with chaotic amplitude modulation
                amp_mod = 1.0 + 0.5 * np.sin(scale * x_scaled[i] * 2.0)
                multiscale += amp_mod * np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.8) * \
                             np.exp(-scale * np.abs(x_scaled[i]))
        
        # Chaotic transition regions with fractal boundary effects
        sharpness = 0.0
        for i in range(self.dim):
            # Fractal transition with chaotic steepness variations
            steep1 = 20.0 + 5.0 * np.sin(i * 0.7)
            steep2 = 25.0 + 3.0 * np.cos(i * 0.5)
            sig1 = 1.0 / (1.0 + np.exp(-steep1 * (x_scaled[i] - 0.4)))  # Increased chaos
            sig2 = 1.0 / (1.0 + np.exp(-steep2 * (x_scaled[i] + 0.4)))  # Increased chaos
            sharpness += (sig1 - 0.5)**3 + (sig2 - 0.5)**3  # Cubic sharpness
        
        # Chaotic noise component for added complexity
        noise = 0.0
        for i in range(self.dim):
            # Chaotic noise with exponential growth
            noise += np.sin(x_scaled[i] * 10.0) * np.cos(x_scaled[i] * 8.0) * \
                    np.exp(-np.abs(x_scaled[i]) * 2.0)
        
        # Combined function with chaotic weighted components
        return 1.2 * fractal + 1.8 * attractor + 0.8 * complexity + 0.6 * multiscale + 0.7 * sharpness + 0.3 * noise