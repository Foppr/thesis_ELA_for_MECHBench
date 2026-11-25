import numpy as np

class AdaptiveTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        normalized_x = x * np.pi / 5.0
        
        # Base trigonometric components with adaptive frequencies
        base_trig = np.sum(np.sin(normalized_x) * np.cos(normalized_x) + 
                          np.sin(2 * normalized_x) * np.cos(2 * normalized_x))
        
        # Adaptive frequency modulation based on input magnitude
        adaptive_freq = np.sum((1 + 0.5 * np.sin(x)) * np.sin(3 * normalized_x) * 
                              (1 + 0.3 * np.cos(x)) * np.cos(4 * normalized_x))
        
        # Phase-shifted harmonic components with varying amplitudes
        phase_shifted = np.sum(np.sin(normalized_x + np.pi/4) * np.cos(normalized_x + np.pi/6) +
                              np.sin(normalized_x - np.pi/3) * np.cos(normalized_x - np.pi/5))
        
        # Exponentially decaying harmonic series with modified decay rates
        decay_harmonics = np.sum(np.exp(-0.5*np.abs(x)) * (np.sin(10 * normalized_x) + 
                                                      np.cos(15 * normalized_x)) +
                               np.exp(-0.3*np.abs(x)**2) * (np.sin(20 * normalized_x) + 
                                                      np.cos(25 * normalized_x)))
        
        # Multi-scale sinusoidal interference patterns with altered frequencies
        interference = 0.6 * np.sum(np.sin(6 * normalized_x) * np.cos(8 * normalized_x) +
                                  np.sin(9 * normalized_x) * np.cos(13 * normalized_x))
        
        # Nested oscillatory components with frequency ratios
        nested_osc = 0.35 * np.sum(np.sin(np.pi * normalized_x) * np.cos(np.pi * normalized_x) +
                                np.sin(2 * np.pi * normalized_x) * np.cos(2 * np.pi * normalized_x))
        
        # Chaotic phase modulation using fractional Brownian motion approximation
        chaotic_phase = 0.35 * np.sum(np.sin(normalized_x + np.sin(x)) * 
                                   np.cos(normalized_x + np.cos(x)))
        
        # Power-law amplitude scaling with exponential decay - modified exponents
        power_decay = 0.2 * np.sum((np.abs(x) ** 1.7) * np.sin(3 * normalized_x) +
                                  (np.abs(x) ** 2.3) * np.cos(5 * normalized_x))
        
        # Resonance-like interactions between components - modified weights
        resonance = 0.4 * np.sum(np.sin(normalized_x) * np.cos(2 * normalized_x) *
                               np.sin(3 * normalized_x) * np.cos(4 * normalized_x))
        
        # Additional nonlinear interaction terms for increased complexity
        nonlinear_interaction = 0.15 * np.sum(np.sin(x**2) * np.cos(x**3) + 
                                            np.sin(x**1.5) * np.cos(x**2.5))
        
        # Combined landscape with weighted contributions
        return 1.1 * (base_trig + adaptive_freq + phase_shifted + decay_harmonics + 
                     interference + nested_osc + chaotic_phase + power_decay + resonance + nonlinear_interaction)