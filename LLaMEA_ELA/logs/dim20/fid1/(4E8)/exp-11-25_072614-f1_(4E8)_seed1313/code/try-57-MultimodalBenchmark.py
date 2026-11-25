import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with enhanced exponential decay and sinusoidal modulation
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-r / 2.0) * (1.0 + 0.9 * np.sin(r * 1.5) * np.cos(r * 0.8))
        
        # Enhanced trigonometric interference with multiple frequencies
        trig_interference = np.sum(np.cos(4.0 * x) * np.sin(6.5 * x) * np.exp(-r / 3.0))
        
        # Chaotic component with modified sine-cosine interactions
        chaotic = np.sum(np.sin(x**2 + 0.7) * np.cos(x * 1.3 + 0.4) * np.sin(r * 0.5))
        
        # Increased polynomial radial term with higher degree and modified coefficients
        polynomial = 0.008 * r**6
        
        # Novel cross-term interactions with trigonometric modulation
        cross_terms = 0.025 * np.sum(x[:-1] * x[1:] * np.sin(r * 1.2) * np.cos(r * 0.7))
        
        # Additional harmonic component for increased multimodality
        harmonic = 0.015 * np.sum(np.sin(5.0 * x) * np.cos(3.0 * x))
        
        # Combine all components with adjusted weights
        return radial + 0.4 * trig_interference + 0.25 * chaotic + polynomial + cross_terms + harmonic