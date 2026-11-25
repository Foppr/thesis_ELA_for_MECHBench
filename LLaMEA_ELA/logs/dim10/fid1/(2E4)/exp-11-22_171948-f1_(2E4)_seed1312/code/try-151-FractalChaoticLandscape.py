import numpy as np

class FractalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponentially decaying sinusoidal components with enhanced fractal scaling
        for i in range(self.dim):
            freq = 2 ** (i % 8 + 1)  # Changed from %7 to %8 and shifted by 1
            scale = 1.0 / (1.0 + 0.6 * i)  # Increased scaling factor
            component = np.sin(freq * x[i]) * np.exp(-0.4 * np.abs(x[i])) * scale  # Increased decay rate
            result += 0.8 * component**2  # Increased weight
        
        # Trigonometric coupling with enhanced phase modulation
        for i in range(self.dim - 1):
            phase_mod = np.sin(np.pi * (x[i] + x[i+1]) / 2.0) * np.cos(np.pi * (x[i] - x[i+1]) / 5.0)  # Enhanced phases
            coupling = np.sin(11 * (x[i] - x[i+1])) * phase_mod  # Changed frequency from 10 to 11
            result += 0.7 * coupling**2  # Increased weight
        
        # Multi-scale fractal-like ridge structures with enhanced self-similarity
        for i in range(self.dim):
            ridge_freqs = [5, 9, 13, 17, 21]  # Shifted frequencies
            ridge_sum = 0.0
            for freq in ridge_freqs:
                ridge_sum += np.sin(freq * x[i]) * np.exp(-0.08 * (freq - 15)**2)  # Changed decay rate and center
            result += 1.0 * ridge_sum**2  # Increased weight
        
        # Exponentially weighted long-range interactions with enhanced scaling
        for i in range(self.dim):
            interaction_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = np.exp(-0.7 * np.abs(i - j))  # Increased decay rate
                    interaction_sum += weight * (x[i] - x[j])**2
            result += 0.6 * interaction_sum  # Increased weight
        
        # Adaptive conditioning based on local curvature and dimensionality with hyperbolic sine
        curvature = 0.0
        for i in range(self.dim):
            curvature += np.abs(np.cos(x[i])) + np.sinh(0.6 * x[i])**2  # Added hyperbolic sine
        conditioning = 1.0 + 0.8 * np.tanh(curvature)  # Increased conditioning factor
        result *= conditioning
        
        # Asymmetric basin structure with enhanced symmetry breaking and quantum interference
        asymmetry = 0.0
        for i in range(self.dim):
            asymmetry += (x[i] ** 6) * np.sin(0.8 * x[i]) + 0.15 * np.sin(22 * x[i]) * np.cos(17 * x[i])  # Increased power and quantum terms
        result += 0.6 * asymmetry  # Increased weight
        
        # Additional chaotic noise injection with enhanced sensitivity and interference
        chaos_noise = 0.0
        for i in range(self.dim):
            chaos_noise += np.sin(17 * x[i]) * np.cos(21 * x[i]) * np.exp(-0.2 * np.abs(x[i])) + 0.06 * np.sin(27 * x[i])  # Added quantum interference
        result += 0.5 * chaos_noise**2  # Increased weight
        
        # Quantum-like interference patterns
        quantum_pattern = 0.0
        for i in range(self.dim):
            quantum_pattern += np.sin(4 * x[i] + np.pi/5) * np.cos(4 * x[i] - np.pi/7) * np.exp(-0.12 * x[i]**2)
        result += 0.4 * quantum_pattern**2  # Added quantum pattern weight
        
        # Final fractal normalization and enhanced noise sensitivity
        result /= self.dim
        result += 0.15 * np.sum(np.abs(x)**6) / self.dim  # Increased noise sensitivity
        
        return result