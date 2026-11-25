import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component with chaotic sine-cosine patterns and nested recursion
        fractal = 0.0
        for i in range(self.dim):
            freq = 3.0 + 1.5 * np.sin(x_scaled[i] * 4.0)
            amp = 1.2 + 0.5 * np.cos(x_scaled[i] * 3.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.3) * \
                      np.sin(freq * x_scaled[i] * 0.7) * np.cos(freq * x_scaled[i] * 1.2)
        
        # Dynamic attractor fields with chaotic center positions and multi-scale strength
        attractor = 0.0
        for i in range(self.dim):
            center1 = np.sin(i * 0.8 + np.sin(x_scaled[i] * 2.0)) * 0.9
            center2 = np.cos(i * 0.5 + np.cos(x_scaled[i] * 1.5)) * 0.7
            strength1 = 1.5 + 0.4 * np.sin(i * 0.9 + np.cos(x_scaled[i] * 2.5))
            strength2 = 1.2 + 0.3 * np.cos(i * 0.6 + np.sin(x_scaled[i] * 1.8))
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            
            attractor += strength1 * np.exp(-dist1 * 0.5) + strength2 * np.exp(-dist2 * 0.7)
        
        # Enhanced complexity with chaotic interaction terms and nested dimension coupling
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction range
                weight = 2.0 / (1.0 + np.abs(i - j)**1.5)  # Non-linear weight decay
                complex_term = np.sin(x_scaled[i] + x_scaled[j]) * \
                              np.cos(x_scaled[i] - x_scaled[j]) * \
                              np.sin(x_scaled[i] * x_scaled[j])
                complexity += weight * complex_term
        
        # Multi-scale fractal with chaotic frequency modulation and exponential decay
        multiscale = 0.0
        for scale in [1, 2, 3, 6]:  # Added scale 6 and changed frequencies
            for i in range(self.dim):
                freq_mod = 1.0 + 0.3 * np.sin(i * 0.4 + x_scaled[i] * 2.0)
                multiscale += freq_mod * np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.8) * \
                             np.exp(-scale**1.5 * np.abs(x_scaled[i]))
        
        # Chaotic sharp transition regions with multiple sigmoidal boundaries
        sharpness = 0.0
        for i in range(self.dim):
            sigs = []
            for k in range(5):  # Increased number of sigmoidal transitions
                boundary = (k - 2) * 0.4 + 0.1 * np.sin(x_scaled[i] * 3.0)
                steepness = 20.0 + 5.0 * np.cos(i * 0.3)
                sig = 1.0 / (1.0 + np.exp(-steepness * (x_scaled[i] - boundary)))
                sigs.append(sig)
            sharpness += sum((s - 0.5)**2 for s in sigs)
        
        # Chaotic coupling between all components
        return 0.8 * fractal + 1.5 * attractor + 0.6 * complexity + 0.7 * multiscale + 0.5 * sharpness