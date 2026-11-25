import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term - encourages convergence to center
        basin = 0.1 * np.sum(x**2)
        
        # Enhanced multimodal grid terms with chaotic harmonic interactions
        grid_terms = 0.0
        for i in range(self.dim):
            # Create complex periodic structure with varying frequencies and phases
            freq1 = 0.8 + 0.2 * np.sin(0.6 * i)
            freq2 = 0.4 + 0.3 * np.cos(0.4 * i)
            phase1 = 0.2 * np.sin(0.7 * i)
            phase2 = 0.3 * np.cos(0.5 * i)
            
            grid_terms += np.sin(freq1 * x[i] + phase1) * np.cos(freq2 * x[i] + phase2)
            
            # Add higher frequency components for increased complexity
            grid_terms += 0.5 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i])
            
            # Add cross-terms between dimensions with chaotic coupling coefficients
            if i > 0:
                coupling1 = 0.2 + 0.1 * np.sin(0.5 * i)
                coupling2 = 0.15 + 0.05 * np.cos(0.7 * i)
                grid_terms += coupling1 * np.sin(coupling2 * x[i-1]) * np.cos(coupling2 * x[i])
            
            # Add additional nonlinear interaction terms with adaptive scaling
            adaptive_scale = 0.3 + 0.15 * np.sin(0.9 * i)
            grid_terms += adaptive_scale * np.sin(2.0 * x[i])**3
            
            # Introduce chaotic modulation based on position
            chaos_mod = 1.0 + 0.4 * np.sin(2.5 * x[i])
            grid_terms += 0.15 * chaos_mod * np.sin(2.5 * x[i]) * np.cos(2.0 * x[i])
            
            # Add polynomial interaction terms for increased complexity
            grid_terms += 0.08 * x[i]**4 * np.sin(x[i])
            grid_terms += 0.06 * x[i]**5 * np.cos(0.3 * x[i])
        
        # Add enhanced chaotic interaction terms between all dimensions
        chaotic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i < self.dim and j < self.dim:
                    coupling_strength = 0.08 + 0.03 * np.sin(0.4 * (i + j))
                    chaotic_interaction += coupling_strength * np.sin(x[i]) * np.cos(x[j])
                    
                    # Add higher-order cross-dimensional interactions
                    chaotic_interaction += 0.02 * np.sin(x[i]**3) * np.cos(x[j]**3)
        
        # Add exponential barrier terms to increase conditioning difficulty
        exp_barrier = 0.0
        for i in range(self.dim):
            exp_barrier += 0.8 * np.exp(-0.15 * x[i]**2) * np.sin(2.5 * x[i])
        
        # Add additional harmonic interference patterns
        harmonic_interference = 0.0
        for i in range(self.dim):
            harmonic_interference += 0.3 * np.sin(1.2 * x[i]) * np.cos(1.8 * x[i]) * np.sin(0.9 * x[i])
        
        # Combine all terms with different weights to create challenging landscape
        return basin + 0.9 * grid_terms + 2.0 * np.sum(np.abs(x)) / self.dim + 0.7 * chaotic_interaction + exp_barrier + harmonic_interference