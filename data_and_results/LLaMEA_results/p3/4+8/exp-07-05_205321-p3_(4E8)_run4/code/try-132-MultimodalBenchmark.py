import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Asymmetric radial component with chaotic modulation
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**2.0) * (1.0 + 0.5 * np.sin(12 * r) * np.cos(7 * r) + 0.3 * np.sin(15 * r**1.5))
        
        # Angular components with chaotic phase shifts and asymmetric interactions
        angular = 0.0
        for i in range(self.dim):
            phase_shift = np.sin(i * 0.785)  # Chaotic phase shift
            angular += np.sin((i + 1) * np.pi * x_norm[i] + phase_shift) * np.cos((i + 1) * np.pi * x_norm[i] + phase_shift)
            if i > 0:
                angular += 0.15 * np.sin(3 * np.pi * x_norm[i-1] + 0.5) * np.sin(3 * np.pi * x_norm[i] - 0.3)
        
        # Highly chaotic periodic term with varying amplitudes
        periodic = 0.0
        for i in range(self.dim):
            freq = 2 * (i + 1) + np.sin(i * 0.5)
            amp = 0.4 + 0.2 * np.sin(i * 0.3)
            periodic += amp * np.sin(freq * np.pi * x_norm[i] + 0.2 * i) * np.cos(freq * np.pi * x_norm[i] - 0.1 * i)
        
        # Cross-dimensional coupling with non-linear interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.1 * np.sin(6 * np.pi * x_norm[i] + 0.3) * np.cos(5 * np.pi * x_norm[j] - 0.2) * (1 + 0.1 * np.sin(i * j))
        
        # Add a chaotic noise component to increase ruggedness
        noise = 0.05 * np.sum(np.sin(20 * x_norm + np.random.rand(self.dim) * 2 * np.pi))
        
        # Combine all components with adjusted weights
        return 0.3 * radial + 0.25 * angular + 0.25 * periodic + 0.15 * cross_term + 0.05 * noise + 1.0