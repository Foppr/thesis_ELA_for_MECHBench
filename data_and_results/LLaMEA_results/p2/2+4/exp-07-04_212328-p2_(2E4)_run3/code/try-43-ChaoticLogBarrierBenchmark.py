import numpy as np

class ChaoticLogBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base quadratic term with conditioning
        f = 0.5 * np.sum(x**2)
        
        # Add logarithmic barrier terms with multiple local minima
        for i in range(self.dim):
            # Logarithmic barriers at specific points
            barrier_terms = 0
            for center in [-4.0, -2.0, 0.0, 2.0, 4.0]:
                dist = np.abs(x[i] - center)
                if dist < 0.5:
                    barrier_terms += 10 * np.log(0.5 / (0.5 - dist + 1e-10))
                else:
                    barrier_terms += 0.1 * dist**2
            f += barrier_terms
            
        # Add polynomial coupling with varying degrees
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Higher degree polynomial coupling
                f += 0.3 * (x[i]**3 + x[j]**3) * np.sin(2 * x[i] * x[j])
                
        # Add multi-scale harmonic oscillations with exponential decay
        for i in range(self.dim):
            freq = 1
            for scale in range(1, 6):
                f += 0.2 * np.sin(freq * x[i]) * np.cos(2 * freq * x[i]) * np.exp(-0.1 * scale)
                freq *= 3
                
        # Add chaotic phase interactions with nested structure
        phase_sum = 0
        for i in range(self.dim):
            phase_sum += np.sin(10 * x[i] + np.sin(5 * x[i]))
        f += 0.4 * np.sin(phase_sum)
        
        # Add nested harmonic oscillations with varying amplitudes
        for i in range(self.dim):
            amp = 0.5
            for k in range(1, 8):
                f += amp * np.sin(k * x[i]) * np.cos(k * x[i] * 0.5)
                amp *= 0.7
                
        # Add cross-dimensional coupling with exponential scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f += 0.15 * np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(5 * (x[i] + x[j]))
                
        # Add fractal-like self-similarity with recursive harmonic structure
        for i in range(self.dim):
            f += 0.25 * np.sin(15 * np.sin(3 * x[i])) * np.cos(12 * np.sin(2 * x[i]))
            
        # Add sharp transition regions with sigmoidal functions
        for i in range(self.dim):
            f += 0.3 * (1 / (1 + np.exp(-10 * (x[i] - 1.5))) - 1 / (1 + np.exp(-10 * (x[i] + 1.5))))
            
        # Add multi-modal structure with varying scales
        for i in range(self.dim):
            f += 0.1 * np.sin(20 * x[i]) * np.cos(15 * x[i]) * np.sin(10 * x[i])
            
        # Add noise component with chaotic modulation
        noise = 0
        for i in range(self.dim):
            noise += np.sin(13 * x[i]) * np.cos(7 * x[i]) * np.sin(5 * x[i])
        f += 0.05 * noise
        
        return f