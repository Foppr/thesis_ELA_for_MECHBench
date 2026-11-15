import numpy as np

class OscillatoryRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Base quadratic component with global minimum at origin
        quadratic = np.sum(x_norm**2)
        
        # Multi-scale oscillatory component with varying frequencies and amplitudes
        oscillatory = 0.0
        frequencies = [2, 5, 8, 12, 20]
        amplitudes = [1.5, 1.2, 0.8, 0.6, 0.4]
        for freq, amp in zip(frequencies, amplitudes):
            oscillatory += amp * np.sin(freq * np.pi * x_norm) * np.cos(freq * np.pi * x_norm**2)
        
        # Cross-dimensional interaction terms with varying strength
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.3 * np.sin(10 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(5 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Rugged component with multiple local minima using Gaussian-like peaks
        rugged = 0.0
        num_peaks = min(20, 2 * self.dim)
        peak_positions = np.random.uniform(-1, 1, (num_peaks, self.dim))
        for i in range(num_peaks):
            peak_pos = peak_positions[i]
            distance = np.sum((x_norm - peak_pos)**2)
            rugged += 2.0 * np.exp(-10 * distance) + 0.5 * np.exp(-5 * distance)
        
        # Fractional power component to introduce non-smoothness and directional bias
        fractional = np.sum(np.abs(x_norm)**1.7 + 0.3 * np.sin(15 * np.pi * x_norm))
        
        # Control parameter for overall landscape complexity
        complexity = 0.5 + 0.5 * np.sin(0.5 * np.sum(x_norm))
        
        # Combine components with dynamic weighting
        result = complexity * (0.4 * quadratic + 0.3 * oscillatory + 0.2 * interaction + 0.1 * rugged + 0.05 * fractional)
        
        # Add small random noise for robustness
        noise = 0.01 * np.random.random()
        
        return result + noise