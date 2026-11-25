import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term - encourages convergence to center
        basin = 0.1 * np.sum(x**2)
        
        # Multimodal oscillation terms - create complex periodic structure
        oscillation_terms = 0.0
        for i in range(self.dim):
            # Base chaotic oscillatory components with varying frequencies
            freq1 = 0.8 + 0.2 * np.sin(0.6 * i)
            freq2 = 0.4 + 0.3 * np.cos(0.4 * i)
            oscillation_terms += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
            
            # Add higher harmonic components for increased complexity
            oscillation_terms += 0.3 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i])
            
            # Introduce cross-dimensional coupling with chaotic coefficients
            if i > 0:
                coupling1 = 0.2 + 0.05 * np.sin(0.5 * i)
                coupling2 = 0.15 + 0.08 * np.cos(0.7 * i)
                oscillation_terms += coupling1 * np.sin(coupling2 * x[i-1]) * np.cos(coupling2 * x[i])
            
            # Add adaptive nonlinear interaction terms
            adaptive_scale = 0.25 + 0.1 * np.sin(0.9 * i)
            oscillation_terms += adaptive_scale * np.sin(1.8 * x[i])**3
            
            # Introduce chaotic modulation based on position
            chaos_mod = 1.0 + 0.25 * np.sin(2.5 * x[i])
            oscillation_terms += 0.12 * chaos_mod * np.sin(2.4 * x[i]) * np.cos(2.0 * x[i])
            
            # Add polynomial interaction terms for increased complexity
            oscillation_terms += 0.06 * x[i]**3 * np.sin(x[i])
            oscillation_terms += 0.04 * x[i]**5 * np.cos(0.3 * x[i])
            
            # Add novel exponential interaction terms
            oscillation_terms += 0.08 * np.exp(-0.2 * np.abs(x[i])) * np.sin(3.0 * x[i])
            oscillation_terms += 0.05 * np.exp(-0.1 * x[i]**2) * np.cos(2.0 * x[i])
        
        # Add chaotic cross-dimensional interaction terms with enhanced coupling
        chaotic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i < self.dim and j < self.dim:
                    coupling_strength = 0.08 + 0.03 * np.sin(0.4 * (i + j))
                    chaotic_interaction += coupling_strength * np.sin(x[i]) * np.cos(x[j])
                    
                    # Add higher-order cross-dimensional interactions
                    chaotic_interaction += 0.02 * np.sin(x[i]**3) * np.cos(x[j]**3)
                    
                    # Add novel exponential cross-dimensional terms
                    chaotic_interaction += 0.015 * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * np.sin(2.0 * x[i] * x[j])
        
        # Add enhanced conditioning through modified penalty terms with new structure
        conditioning_penalty = 0.0
        for i in range(self.dim):
            conditioning_penalty += 0.5 * np.abs(x[i])**1.8 * np.sin(3.0 * x[i]) + 0.2 * np.exp(-0.1 * np.abs(x[i])) * np.cos(4.0 * x[i])
        
        # Add new exponential barrier terms with different exponents and coefficients
        exp_barrier = 0.0
        for i in range(self.dim):
            exp_barrier += 0.6 * np.exp(-0.15 * x[i]**2) * np.sin(2.5 * x[i]) + 0.3 * np.exp(-0.3 * x[i]**3) * np.cos(1.5 * x[i])
        
        # Add novel harmonic interference patterns with complex phase relationships
        harmonic_interference = 0.0
        for i in range(self.dim):
            harmonic_interference += 0.2 * np.sin(x[i]) * np.cos(2.0 * x[i]) * np.sin(3.0 * x[i])
            harmonic_interference += 0.15 * np.sin(0.5 * x[i])**2 * np.cos(1.5 * x[i])**2
        
        # Combine all terms with different weights to create challenging landscape
        return basin + 0.8 * oscillation_terms + 2.0 * np.sum(np.abs(x)) / self.dim + 0.6 * chaotic_interaction + exp_barrier + 0.3 * conditioning_penalty + 0.4 * harmonic_interference