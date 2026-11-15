import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base quadratic term
        f = 0.5 * np.sum(x**2)
        
        # Add chaotic gradient components with time-delayed feedback
        chaotic_sum = 0
        for i in range(self.dim):
            # Time-delayed chaotic dynamics
            delay = 1 + int(i * 0.3) % 3
            if i >= delay:
                x_delayed = x[i - delay]
            else:
                x_delayed = 0.0
                
            # Chaotic map with parameter modulation
            a = 3.8 + 0.2 * np.sin(i * 0.7)
            b = 0.1 + 0.05 * np.cos(i * 0.5)
            chaotic_val = np.sin(a * x[i] + b * x_delayed + np.sin(x[i] * 2.0))
            chaotic_sum += chaotic_val * np.cos(x[i] * 1.5 + np.sin(x[i] * 0.8))
            
        f += 1.2 * chaotic_sum
        
        # Multi-scale harmonic oscillations
        harmonic_sum = 0
        for i in range(self.dim):
            # Multiple frequencies with varying amplitudes
            freqs = [1.0, 2.0, 3.0, 4.0]
            amps = [1.0, 0.7, 0.5, 0.3]
            for freq, amp in zip(freqs, amps):
                harmonic_sum += amp * np.sin(x[i] * freq + np.sin(x[i] * freq * 0.5))
                
        f += 0.8 * harmonic_sum
        
        # Add gradient complexity with polynomial interactions
        poly_grad = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Polynomial gradient terms
                poly_grad += (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j] * 0.3)
                
        f += 0.6 * poly_grad
        
        # Intermittent chaotic regions
        intermittent_sum = 0
        for i in range(self.dim):
            # Create intermittent behavior with logistic map
            r = 3.9 + 0.1 * np.sin(i * 0.4)
            logistic_val = r * x[i] * (1 - x[i])
            intermittent_sum += np.sin(logistic_val * 2.0) * np.cos(x[i] * 1.2)
            
        f += 0.9 * intermittent_sum
        
        # Add multi-scale coupling with varying strengths
        coupling_sum = 0
        for level in range(3):
            strength = 0.5 + 0.3 * np.sin(level * 0.8)
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    coupling = strength * np.sin(x[i] * x[j] * 0.4 + 
                                                np.cos(x[i] + x[j]) * 0.3 * (level + 1))
                    coupling_sum += coupling
                    
        f += 1.0 * coupling_sum
        
        # Add phase-locked oscillatory components
        phase_sum = 0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * 2.5 + np.sin(x[i] * 1.5) + np.sin(x[i] * 0.8))
            
        f += 0.7 * phase_sum
        
        # Add temporal dynamics with exponential decay
        temporal_sum = 0
        for i in range(self.dim):
            temporal_sum += np.exp(-0.1 * np.abs(x[i])) * np.cos(x[i] * 3.0)
            
        f += 0.5 * temporal_sum
        
        # Add complex cross-dimensional interactions
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Complex interaction with multiple harmonic components
                cross_sum += (np.sin(x[i] * x[j] * 0.5) + 
                             np.cos(x[i] * x[j] * 0.3) + 
                             np.sin(x[i] + x[j]) * 0.2)
                
        f += 0.8 * cross_sum
        
        return f